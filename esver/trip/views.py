from django.shortcuts import render
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"trip/index.html")
def register(request):
    return render(request,"trip/register.html")
def places(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"trip/places.html",{'catagory':catagory})
def placesview(request,name):
    if (Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(catagory__name=name)
        return render(request,"trip/products/index.html",{'products':products,"category_name":name})
    else:
        message.warning(request,"No Such Catagory Found")
        return redirect('places')
