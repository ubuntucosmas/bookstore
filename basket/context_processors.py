
from .basket import Basket  # Import your Basket class

def basket(request):
    basket = Basket(request)
    return {
        'basket': basket
    }

