from django.views.generic import TemplateView
from apps.partners.models import Partner
from apps.blog.models import Post
from apps.product.models import Brand, Category


class HomeView(TemplateView):
    template_name = 'index.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['partners'] = Partner.objects.all()
        context['brands'] = Brand.objects.all()[:8]
        context['posts'] = (
            Post.objects.prefetch_related('tags').order_by('created_at')
        )
        context['categories'] = Category.objects.filter(
            is_active=True, parent__isnull=True
        ).prefetch_related('children')
        context['category_limit']=8
        return context
