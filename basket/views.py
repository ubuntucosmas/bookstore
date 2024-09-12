
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .basket import Basket  # Import your Basket class
from store.models import Product

def add_to_basket(request):
    basket = Basket(request)  # Create a new Basket instance
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided

        if not product_id:
            return JsonResponse({'error': 'No product ID provided'}, status=400)
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=quantity )
        # Return JSON response with product title and basket details
        response = {
            'message': f'{quantity} {product.title} has been added to your basket successfully.',
            'product_title': product.title,  # Add the product title to the response
            'basket_item_count': len(basket.basket),  # Optional
            'basket_total_price': sum(item['quantity'] * float(item['price']) for item in basket.basket.values())  # Optional
        }
        return JsonResponse(response)
    # If the request method is not POST, return a method not allowed response
    return JsonResponse({'error': 'Invalid request method'}, status=405)



def basket_summary_view(request):
    basket = Basket(request)
    context = {
        'basket': basket,
    }
    trending = Product.objects.filter(title="Nike").first()
    popular = Product.objects.filter(price=388).first()
    soon = Product.objects.filter(slug="t-shirt").first()

    context = {'basket': basket,'trending':trending,'popular':popular,'soon':soon}
    return render(request, './store/basket/basket_summary.html', context)


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.remove(product)
    return redirect('basket:view_basket')  # Redirect to the basket page

def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket:view_basket')  # Redirect back to the basket page