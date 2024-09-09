from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product/single.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    #return all the products in the category above(category)
    products = Product.objects.filter(category=category) 
    return render(request, 'store/product/category.html', {'category': category, 'products': products})