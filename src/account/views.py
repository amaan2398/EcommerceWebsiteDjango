from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Address
from cart.models import Cart, Shipment
from product.models import Product


def cart_data_add(cid):
    data = Cart.objects.filter(customer_id=cid,shipment=False)
    data = dict({"count":len(data)})
    return data

# Create your views here.
def register(request):
    if request.method == "POST":
        uname = request.POST['uname']

        fname = request.POST['fname']
        lname = request.POST['lname']
        
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        postcode = request.POST['postcode']

        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 == pass2:
            if User.objects.filter(username = uname).exists():
                messages.info(request,"Username taken ...")
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email taken ...")
                return redirect("register")
            else:
                user = User.objects.create_user(username = uname,password = pass1, email = email,first_name = fname, last_name = lname)
                user.save()
                del user
                user = User.objects.get(username = uname)
                address = Address(customer_id=user.id,street_address=address,city=city,state=state,country=country,postcode=postcode)
                address.save()
                messages.info(request,"Account Created")
                return redirect("login")
        else:
            messages.info(request,"Password not matching ...")
            return redirect("register")
    elif request.method == "GET":
        if request.user.id == None:
            return render(request,"accounts/register.html",{})
        else:
            return HttpResponseNotFound()

def login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        user = auth.authenticate(username = uname, password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Wrong username or password...")
            return redirect("login")
    elif request.method == "GET":
        if request.user.id == None:
            return render(request,"accounts/login.html",{})
        else:
            return HttpResponseNotFound()

def logout(request):
    auth.logout(request)
    return redirect("/")

def profile(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        user = User.objects.get(id = request.user.id)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect("profile")
    elif request.method == "GET":
        data = request.user
        address = Address.objects.filter(customer_id=data.id)
        cdata = cart_data_add(request.user.id)
        sdata = Shipment.objects.filter(customer_id= request.user.id)
        fdata = []
        for i in sdata:
            c_data = Cart.objects.filter(bill_id=i.id)
            #cdata = Cart.objects.filter(customer_id=request.user.id,shipment=False)
            tamount = 0
            for j in c_data:
                t_d = Product.objects.filter(id=j.product_id)
                tamount += t_d[0].price * j.product_quantity
            fdata.append({'id':i.id,'tamount':tamount})
        return render(request,"accounts/profile.html",{"data" : data,"address":address,"cdata":cdata,'sdata':sdata,'fdata':fdata})

def edit_address(request):
    if request.method == "POST":
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        postcode = request.POST['postcode']
        address = Address(customer_id=request.user.id,street_address=address,city=city,state=state,country=country,postcode=postcode,default_add=False)
        address.save()
        return redirect("profile")
    elif request.method == "GET":
        data = request.user
        address = Address.objects.filter(customer_id=data.id)
        cnt = len(address)
        cdata = cart_data_add(request.user.id)
        return render(request,"accounts/edit_address.html",{"data" : data,"address":address,"cnt":cnt,"cdata":cdata})

def remove_address(request,id):
    data = Address.objects.filter(id = id)
    if data[0].default_add == True:
        data.delete()
        del data
        try:
            data = Address.objects.get(customer_id=request.user.id)
        except MultipleObjectsReturned:
            data = Address.objects.get(customer_id=request.user.id)[0]
        data.default_add = True
        data.save()
    else:
        data.delete()
    return redirect("edit_address")