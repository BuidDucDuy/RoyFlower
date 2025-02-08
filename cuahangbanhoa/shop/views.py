from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
# Create your views here.

def base(request):
    products = Product.objects.all()
    categories = {}
    for product in products :
        category_name = dict(product.category_choices)[product.category]
        if category_name not in categories:
            categories[category_name] = []
        categories[category_name].append(product)
    return render(request,"shop/base.html" , {'products': products, 'categories': categories})