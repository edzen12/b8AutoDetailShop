from django.urls import path
from apps.product.views import (HomeView, CategoryView, MarkaView, 
                                SearchView, ToggleWishlistView, WishlistView)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('marka/<slug:slug>/', MarkaView.as_view(), name='marka'),
    path('search/', SearchView.as_view(), name='search'),
    path('wishlist/<int:product_id>', ToggleWishlistView.as_view(), name='wishlist_toggle'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
]
