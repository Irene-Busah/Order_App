from http.client import HTTPResponse
from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'home.html'

class ProductCreate(CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = ['product_name', 'product_type', 'price', 'product_image', 'product_desc']
    
