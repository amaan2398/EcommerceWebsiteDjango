from django.shortcuts import render,redirect
from .models import Cart,Shipment
from product.models import Product
from account.models import Address
from django.contrib.auth.models import User,auth

# Create your views here.
def cart(request):
    a = ['','active','']
    cdata = Cart.objects.filter(customer_id=request.user.id,shipment=False)
    data = []
    tamount = 0
    for i in cdata:
        t_d = Product.objects.filter(id=i.product_id)
        data.append(dict({"p_id":i.product_id,"p_name":t_d[0].name,"price":t_d[0].price,"quantity":i.product_quantity,"amount_t":(t_d[0].price * i.product_quantity)}))
        tamount += t_d[0].price * i.product_quantity
    fdata = dict({"total":tamount})
    cid = request.user.id
    cdata = dict({"count":len(data)})
    address = Address.objects.filter(customer_id=cid)
    return render(request,"product/cart.html",{"a":a,"data":data,"fdata":fdata,"address":address,"cdata":cdata})

def addtocart(request,id):
    cid = request.user.id
    if Cart.objects.filter(customer_id= cid,product_id=id,shipment=False).exists():
        a = Cart.objects.get(customer_id= cid,product_id=id,shipment=False)
        a.product_quantity += 1
        a.save()
        del a
    else:
        a = Cart(customer_id=cid,product_id=id,product_quantity=1,shipment=False)
        a.save()
        del a
    return redirect("/")

def addrm_pro_qut(request,id,v):
    cid = request.user.id
    if v == 1:
        if Cart.objects.filter(customer_id= cid,product_id=id,shipment=False).exists():
            a = Cart.objects.get(customer_id= cid,product_id=id,shipment=False)
            a.product_quantity += 1
            a.save()
            del a
        else:
            a = Cart(customer_id=cid,product_id=id,product_quantity=1,shipment=False)
            a.save()
            del a
    elif v == 0:
        if Cart.objects.filter(customer_id= cid,product_id=id).exists():
            a = Cart.objects.get(customer_id= cid,product_id=id,shipment=False)
            a.product_quantity -= 1
            a.save()
            del a
    if Cart.objects.filter(customer_id= cid,product_id=id)[0].product_quantity == 0:
        a = Cart.objects.filter(customer_id= cid,product_id=id,shipment=False)
        a.delete()
    return redirect("cart")

def pro_remove(request, id):
    cid = request.user.id
    a = Cart.objects.filter(customer_id= cid,product_id=id,shipment=False)
    a.delete()
    return redirect("cart")

def checkout_products(request):
    if request.method == "POST":
        add_id = request.POST['address']
        Cart.objects.filter(customer_id=request.user.id,shipment=False).update(address_id =add_id)
        return redirect("checkout")
    else:
        cid = request.user.id
        #Cart.objects.filter(customer_id= cid,shipment=False).update(shipment = True)
        cdata = Cart.objects.filter(customer_id=request.user.id,shipment=False)
        data = []
        tamount = 0
        for i in cdata:
            t_d = Product.objects.filter(id=i.product_id)
            data.append(dict({"p_id":i.product_id,"p_name":t_d[0].name,"price":t_d[0].price,"quantity":i.product_quantity,"amount_t":(t_d[0].price * i.product_quantity)}))
            tamount += t_d[0].price * i.product_quantity
        fdata = dict({"total":tamount})
        cid = request.user.id
        address = Address.objects.filter(customer_id=cid,id = cdata[0].address_id)
        return render(request,"product/checkout.html",{"data":data,"fdata":fdata,"address":address})

def checkout_shipment(request):
    cdata = Cart.objects.filter(customer_id=request.user.id,shipment=False)
    tamount = 0
    for i in cdata:
        t_d = Product.objects.filter(id=i.product_id)
        tamount += t_d[0].price * i.product_quantity
    s = Shipment(customer_id=request.user.id,total_amount=tamount)
    s.save()
    Cart.objects.filter(customer_id= request.user.id,shipment=False).update(shipment = True,bill_id=s.id)
    return redirect('shipment_id',s.id)

def shipment(request):
    return render(request,'product/shipment.html',{})

def shipment_id(request,id):
    data = Shipment.objects.filter(id=id)
    user = request.user
    cart = Cart.objects.filter(bill_id=id)
    return render(request,'product/shipment_view.html',{'data':data,'user':user,'cart':cart})