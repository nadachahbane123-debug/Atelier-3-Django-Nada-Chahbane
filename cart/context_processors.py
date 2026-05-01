from .models import Cart

def cart_count(request):
    count = 0
    if request.user.is_authenticated:
        try:
            count = request.user.cart.total_items()
        except Cart.DoesNotExist:
            pass
    return {'cart_item_count': count}