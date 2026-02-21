from django.views.generic import TemplateView
from apps.partners.models import Partner
from apps.blog.models import Post


class HomeView(TemplateView):
    template_name = 'index.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['partners'] = Partner.objects.all()
        context['posts'] = (
            Post.objects.prefetch_related('tags').order_by('created_at')
        )
        return context
