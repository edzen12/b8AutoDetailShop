from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True,
        null=True, related_name='children', verbose_name="Родитель"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название бренда")
    slug = models.SlugField(unique=True) 
    logo = models.ImageField(upload_to='brand/', verbose_name="Логотип")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'Бренды'


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products'
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, blank=True, null=True, related_name='products'
    )
    name = models.CharField(verbose_name="Название товара", max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")  
    stock = models.PositiveIntegerField(default=0, verbose_name="Количество товара на складе")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/', verbose_name="Фото")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name 
    
    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'Фотки товаров'
    

class Attribute(models.Model): 
    name = models.CharField(max_length=100, verbose_name="Атрибут")

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'атрибут'
        verbose_name_plural = 'Атрибуты'


class AttributeValue(models.Model): 
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100, verbose_name="Значение")

    def __str__(self):
        return f"{self.attribute.name} {self.value}"
    
    class Meta:
        verbose_name = 'значение атрибута'
        verbose_name_plural = 'Значение атрибутов'


class ProductVariant(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    attributes = models.ManyToManyField(AttributeValue)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    stock = models.PositiveIntegerField(default=0, verbose_name="Количество товара на складе")
    sku = models.CharField(max_length=100, unique=True, verbose_name="артикул товара")

    def __str__(self):
        return f"{self.attribute.name} {self.value}"
    
    class Meta:
        verbose_name = 'вариант товара'
        verbose_name_plural = 'Варианты товаров'


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'