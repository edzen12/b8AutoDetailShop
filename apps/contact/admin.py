from django.contrib import admin
from apps.contact.models import ContactInfo, ContactRequest


admin.site.register(ContactInfo)
admin.site.register(ContactRequest)