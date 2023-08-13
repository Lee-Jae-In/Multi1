from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
# Create your views here.

def center(request) :
    return render(request, 'product/center_info.html')

class ProductList(ListView) :
    model = Product
    ordering = '-pk'