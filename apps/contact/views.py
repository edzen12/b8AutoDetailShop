from django.views.generic import TemplateView
from apps.contact.models import ContactInfo


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contactInfo'] = ContactInfo.objects.latest('-id')
        
        return context