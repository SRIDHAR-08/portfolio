from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

def home_page(request):
    return render(request, 'e_commerce/home.html')


def register(request):
    return render(request, 'e_commerce/register.html') 

def category(request):
    category_data = Catagory.objects.filter(status=0)
    return render(request, 'e_commerce/category.html',{'category_data':category_data}) 

def Cart(request):
    return render(request, 'e_commerce/Cart.html') 

def favourite(request):
    return render(request, 'e_commerce/favourite.html') 

def collectionview(request,id):
    category_data = Catagory.objects.filter(status=0,id=id)
    if category_data:
            Product_data = Product.objects.filter(catagory_id=id)
            return render(request, 'e_commerce/collectionview.html',{'Product_data':Product_data}) 
    else:
        return redirect('e_commerce_home')



