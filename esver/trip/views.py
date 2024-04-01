from django.shortcuts import render
from trip.form import CustomUserForm
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"trip/index.html")

def login(request):
    return render(request,"trip/login.html")


def register(request):
  form=CustomUserForm()
  if request.method=='POST':
    form=CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,"Registration Success You can Login Now..!")
      return redirect('/login')
  return render(request,"trip/register.html",{'form':form})


def places(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"trip/places.html",{'catagory':catagory})
def placesview(request,name):
    if (Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(catagory__name=name)
        return render(request,"trip/products/index.html",{'products':products,"category_name":name})
    else:
        
        return redirect('places')

def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,"trip/products/product_details.html",{"products":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return redirect('collections')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collections')
