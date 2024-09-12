from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.


def all_products(request):
    products = Product.objects.all()
    trending = Product.objects.get(title="Nike")
    popular = Product.objects.get(price=22)
    soon = Product.objects.get(slug="t-shirt")
    context = {'products': products, 'trending':trending,'popular':popular,'soon':soon}
    return render(request, 'store/home.html', context)

def product_detail(request, slug):
    trending = Product.objects.get(title="Nike")

    popular = Product.objects.get(price=388)
    soon = Product.objects.get(slug="t-shirt")
    product = get_object_or_404(Product, slug=slug, in_stock=True)

    context = {'product': product,'trending':trending,'popular':popular,'soon':soon}
    return render(request, 'store/product/single.html', context)

def category_list(request, category_slug):

    trending = Product.objects.get(title="Nike")
    popular = Product.objects.get(price=388)
    soon = Product.objects.get(slug="t-shirt")

    category = get_object_or_404(Category, slug=category_slug)
    #return all the products in the category above(category)
    products = Product.objects.filter(category=category) 

    context = {'category': category, 'products':products, 'trending':trending,'popular':popular,'soon':soon}
    return render(request, 'store/product/category.html', context)