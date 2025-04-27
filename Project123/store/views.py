from django.shortcuts import render, redirect, get_object_or_404
from .models import Shoe, Favorite, Cart

# Create your views here.
def home(request):
    shoes = Shoe.objects.all()
    return render(request, 'home.html', {'shoes': shoes})

def add_to_favorites(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    Favorite.objects.get_or_create(shoe=shoe)
    return redirect('home')

def add_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    Cart.objects.get_or_create(shoe=shoe)
    return redirect('home')

def favorites_list(request):
    favorites = Favorite.objects.all()
    return render(request, 'favorites.html', {'favorites': favorites})

def cart_list(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})

def remove_from_favorites(request, fav_id):
    Favorite.objects.filter(id=fav_id).delete()
    return redirect('favorites')

def remove_from_cart(request, cart_id):
    Cart.objects.filter(id=cart_id).delete()
    return redirect('cart')
