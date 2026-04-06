from django.views.generic import TemplateView, ListView
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404

from apps.cart.utils import get_cart
from apps.partners.models import Partner
from apps.blog.models import Post
from apps.product.models import Marka, Category, Slider, Product, ProductImage


class HomeView(TemplateView):
    template_name = 'index.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = get_cart(self.request)
        context['cart'] = cart
        context['cart_items'] = cart.items.select_related('product')

        context['products'] = Product.objects.prefetch_related(
            Prefetch('images', queryset=ProductImage.objects.all())
        )
        context['partners'] = Partner.objects.all()
        context['sliders'] = Slider.objects.all()
        context['markas'] = Marka.objects.all()[:8]
        context['posts'] = (
            Post.objects.prefetch_related('tags').order_by('created_at')
        )
        context['categories'] = Category.objects.filter(
            is_active=True, parent__isnull=True
        ).prefetch_related('children')
        context['category_limit']=3
        return context


class CategoryView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        categories = category.get_descendants(include_self=True)
        return Product.objects.filter(
            category__in=categories
        ).prefetch_related('images')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, slug=self.kwargs['slug']
        )
        return context
    

class MarkaView(ListView):
    template_name = 'pages/marka.html'
    context_object_name = 'products'

    def get_queryset(self):
        marka = get_object_or_404(Marka, slug=self.kwargs['slug'])
        
        return Product.objects.filter(
            car_models__marka=marka,
        ).distinct().prefetch_related('images')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marka'] = get_object_or_404(
            Marka, slug=self.kwargs['slug']
        )
        return context