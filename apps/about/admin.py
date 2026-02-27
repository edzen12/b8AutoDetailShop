from django.contrib import admin
from apps.about.models import AboutContent, PlusAbout, BlogAbout, Faq, Testimonials


admin.site.register(AboutContent)
admin.site.register(PlusAbout)
admin.site.register(BlogAbout)
admin.site.register(Faq)
admin.site.register(Testimonials)