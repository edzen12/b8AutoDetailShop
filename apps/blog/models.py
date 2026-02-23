from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class Tag(models.Model):
    name = models.CharField(verbose_name="Название тега", max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"#{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("posts_by_tag", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    tags = models.ManyToManyField(Tag, related_name='posts')
    title = models.CharField(verbose_name="Название поста", max_length=150)
    img = models.ImageField(upload_to='Фото', null=True)
    slug = models.SlugField(unique=True)
    description = CKEditor5Field('Описание', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'