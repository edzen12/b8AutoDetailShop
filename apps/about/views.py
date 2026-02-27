from django.views.generic import TemplateView
from apps.partners.models import Partner
from apps.about.models import AboutContent, PlusAbout, BlogAbout, Faq, Testimonials


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutContent'] = AboutContent.objects.latest('-id')
        context['plusAbout'] = PlusAbout.objects.all()[:3]
        context['blogsAbout'] = BlogAbout.objects.all()[:3]
        context['faqs'] = Faq.objects.all()
        context['testimonials'] = Testimonials.objects.all()[:6]

        context['partners'] = Partner.objects.all()

        return context