from django.urls import path
from apps.product.views import HomeView, CategoryView, MarkaView, SearchView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('marka/<slug:slug>/', MarkaView.as_view(), name='marka'),
    path('search/', SearchView.as_view(), name='search'),
]
