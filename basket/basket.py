
# # basket.py
from store.models import Product  # Import Product model


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')

        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)  # convert product ID to string for session key
        if product_id not in self.basket:
            self.basket[product_id] = {
                'price': str(product.price),  # store price as string for serialization
                'quantity': quantity,
                 
            }
        else:
            if update_quantity:
                self.basket[product_id]['quantity'] = quantity
            else:
                self.basket[product_id]['quantity'] += quantity

        self.session.modified = True  # mark session as modified to save

    def remove(self, product):
        """Remove product from the basket."""
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.session.modified = True  # mark session as modified to save

    def clear(self):
        """Clear the basket from the session."""
        self.session['skey'] = {}
        self.session.modified = True

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.basket[str(product.id)]['product'] = product

        for item in self.basket.values():
            item['price'] = float(item['price'])
            yield item

    def get_total_qty(self):
        return sum(item['quantity'] for item in self.basket.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.basket.values())
