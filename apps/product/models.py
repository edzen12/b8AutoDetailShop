from django.db import models
from django.utils.text import slugify


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

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/', verbose_name="Фото")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name 
    

class Attribute(models.Model): 
    name = models.CharField(max_length=100, verbose_name="Атрибут")

    def __str__(self):
        return self.name 


class AttributeValue(models.Model): 
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=100, verbose_name="Значение")

    def __str__(self):
        return f"{self.attribute.name} {self.value}"


class ProductVariant(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    attributes = models.ManyToManyField(AttributeValue)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    stock = models.PositiveIntegerField(default=0, verbose_name="Количество товара на складе")
    sku = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.attribute.name} {self.value}"

