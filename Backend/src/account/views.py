from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Address

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
        return render(request,"accounts/register.html",{})

def login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        user = auth.authenticate(username = uname, password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Wrong email or password...")
            return redirect("login")
    elif request.method == "GET":
        return render(request,"accounts/login.html",{})

def logout(request):
    auth.logout(request)
    return redirect("/")

def profile(request):
    data = request.user
    address = Address.objects.all()
    return render(request,"accounts/profile.html",{"data" : data,"address":address})

def edit_profile(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        data = request.user
        address = Address.objects.all()
        return render(request,"accounts/edit_profile.html",{"data" : data,"address":address})