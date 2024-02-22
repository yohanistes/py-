from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def home(request):
    info= StoreInformation.objects.all().first
    description= StoreInformation.objects.all()
    data={
        'info':info,
        'description':description
    }
    return render(request,'index.html',data)

def product(request):
    Book= book.objects.all()
    data={
        'book':Book
    }
    return render(request,'product.html',data)

def contact(request):
    return render(request,'contact.html')