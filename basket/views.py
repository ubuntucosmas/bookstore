
from django.shortcuts import render, get_object_or_404
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
    return render(request, './store/basket/basket_summary.html', context)


# def basket_add(request):
#     if request.method == 'POST':
#         basket = Basket(request)
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         product = get_object_or_404(Product, id=product_id)
#         basket = request.session.get('basket', {})
#         #basket.add(product=product, qty=product_qty)
#         if product_id in basket:
#             basket[product_id]['product_qty'] += product_qty
#         else:
#             basket[product_id] = {
#                 'name': product.name,
#                 'price': str(product.price),  # Ensure price is a string if DecimalField
#                 'product_qty': product_qty,
#             }

#         # Save the updated basket in the session
#         request.session['basket'] = basket

#         return JsonResponse({'status': 'success', 'message': 'Product added to basket!'})
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

#         # response = JsonResponse({'qty':product_qty})
#         # return HttpResponse(status=400)