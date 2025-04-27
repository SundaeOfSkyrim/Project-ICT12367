from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('favorites/', views.favorites_list, name='favorites'),
    path('cart/', views.cart_list, name='cart'),
    path('add-to-favorites/<int:shoe_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('add-to-cart/<int:shoe_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-favorites/<int:fav_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
]
