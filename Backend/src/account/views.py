from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
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