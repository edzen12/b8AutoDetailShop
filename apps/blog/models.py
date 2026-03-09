from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(
        verbose_name="Название категории", 
        max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("posts_category", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


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
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        verbose_name='Категория', null=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    title = models.CharField(verbose_name="Название поста", max_length=150)
    img = models.ImageField(upload_to='Фото', null=True)
    slug = models.SlugField(unique=True)
    description = CKEditor5Field('Описание', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, 
        related_name='comments', verbose_name="Пост"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, 
        null=True, blank=True, related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.post}" 