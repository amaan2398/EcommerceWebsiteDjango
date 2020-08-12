from django.shortcuts import render
from .models import Product
from cart.models import Cart
#from django.http import HttpResponse

def cart_data_add(cid):
    data = Cart.objects.filter(customer_id=cid)
    data = dict({"count":len(data)})
    return data

# Create your views here.
def index(request):
    data = Product.objects.all()
    for i,j in enumerate(data):
        if len(j.description) > 33:
            data[i].description = j.description[:33]+'...'
    a = ['active','','']
    cdata = cart_data_add(request.user.id)
    return render(request,"index.html",{'data' : data,"a": a,"cdata":cdata})

def product_view(request,id):
    data = Product.objects.get(id = id)
    a = ['','','']
    cdata = cart_data_add(request.user.id)
    return render(request,"product/show_product.html",{"data":data,"a": a,"cdata":cdata})