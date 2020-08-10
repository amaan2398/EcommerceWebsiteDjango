from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    data = [{'name':'pant','price':210.5},{'name':'pant1','price':211.102}]
    return render(request,"index.html",{'data' : data})