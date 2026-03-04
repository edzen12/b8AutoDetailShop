from django.contrib import admin
from apps.blog.models import Tag, Post, Category


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)