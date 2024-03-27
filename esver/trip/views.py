from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    return render(request,"trip/index.html")
def register(request):
    return render(request,"trip/register.html")
def places(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"trip/places.html",{'catagory':catagory})