from django.shortcuts import render,redirect
from .models import Cart
from product.models import Product
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
    cdata = Cart.objects.filter(customer_id=cid,shipment=False)
    cdata = dict({"count":len(data)})
    return render(request,"product/cart.html",{"a":a,"data":data,"fdata":fdata,"cdata":cdata})

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
    cid = request.user.id
    Cart.objects.filter(customer_id= cid,shipment=False).update(shipment = True)
    return render(request,"product/checkout.html",{})