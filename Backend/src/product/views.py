from django.shortcuts import render
from .models import Product
#from django.http import HttpResponse

# Create your views here.
def index(request):
    data = Product.objects.all()
    for i,j in enumerate(data):
        if len(j.description) > 33:
            data[i].description = j.description[:33]+'...'
    return render(request,"index.html",{'data' : data,"a":['active','','']})