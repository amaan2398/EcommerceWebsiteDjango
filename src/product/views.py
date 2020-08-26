from django.shortcuts import render
from .models import Product
from cart.models import Cart
#from django.http import HttpResponse

def cart_data_add(cid):
    data = Cart.objects.filter(customer_id=cid,shipment=False)
    data = dict({"count":len(data)})
    return data

# Create your views here.
def index(request):
    data = Product.objects.all()
    for i,j in enumerate(data):
        if len(j.description) > 20:
            data[i].description = j.description[:20]+'...'
    a = ['active','','']
    cdata = cart_data_add(request.user.id)
    return render(request,"index.html",{'data' : data,"a": a,"cdata":cdata})

def product_view(request,id):
    data = Product.objects.get(id = id)
    a = ['','','']
    cdata = cart_data_add(request.user.id)
    return render(request,"product/show_product.html",{"data":data,"a": a,"cdata":cdata})

def search(request):
    s = request.GET['s']
    lst = s.split(' ')
    rpts = "description LIKE '%"
    rpte = "%'"
    a = ['','','']
    cdata = cart_data_add(request.user.id)
    q ="SELECT * FROM product_product WHERE "
    if len(lst) > 0:
        for i,j in enumerate(lst):
            if i > 0:
                q+=" or "
            q += rpts+j+rpte
        data = Product.objects.raw(q)
        for i,j in enumerate(data):
            if len(j.description) > 20:
                data[i].description = j.description[:20]+'...'
        return render(request,"index.html",{'data' : data,"a": a,"cdata":cdata,"tag":lst})

    else:
        data = Product.objects.all()
        for i,j in enumerate(data):
            if len(j.description) > 20:
                data[i].description = j.description[:20]+'...'
        return render(request,"index.html",{'data' : data,"a": a,"cdata":cdata})