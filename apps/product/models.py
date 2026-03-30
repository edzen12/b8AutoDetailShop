from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q, UniqueConstraint

User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, blank=True,
        null=True, related_name='children', verbose_name="Родитель"
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Marka(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название марки", unique=True)
    slug = models.SlugField(unique=True) 
    logo = models.ImageField(
        upload_to='brand/', verbose_name="Логотип", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'марка'
        verbose_name_plural = 'Марки'


class CarModel(models.Model):
    marka = models.ForeignKey(
        Marka, on_delete=models.CASCADE, 
        related_name='models', verbose_name="Марка"
    )
    name = models.CharField(max_length=100, verbose_name="Модель")
    generation = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Поколение")
    year_from = models.IntegerField(verbose_name="Год выпуска", blank=True, null=True)

    def __str__(self):
        return f"{self.marka.name} {self.name} {self.generation or ''}"

    class Meta:
        verbose_name = 'модель авто'
        verbose_name_plural = 'Модели авто'


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        related_name='products', verbose_name="Категория"
    )
    car_models = models.ManyToManyField(
        CarModel, verbose_name="Модель авто",
        related_name='products'
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

    def get_main_image(self):
        return self.images.filter(is_main=True).first()

    def get_second_image(self):
        return self.images.filter(is_main=False).first()
    
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
    
    def save(self, *args, **kwargs):
        if self.is_main:
            ProductImage.objects.filter(
                product=self.product,
                is_main=True
            ).exclude(pk=self.pk).update(is_main=False)

        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'Фотки товаров'
        constraints = [
            UniqueConstraint(
                fields=['product'],
                condition=Q(is_main=True),
                name='unique_main_image_per_product'
            )
        ]
    

class Attribute(models.Model): 
    name = models.CharField(max_length=100, verbose_name="Атрибут")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        null=True, blank=True, verbose_name="Категория"
    )

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
        unique_together = ['product', 'sku']


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    ) 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'


class Slider(models.Model):
    title = models.CharField(max_length=80, verbose_name="Заголовок")
    image = models.ImageField(upload_to='slider', null=True)
    small_text = models.TextField(verbose_name="Текст описание")
    name_button = models.CharField(max_length=80, verbose_name="Название кнопки")
    link_button = models.CharField(max_length=255, verbose_name="Ссылка кнопки")

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'слайдер'
        verbose_name_plural = 'Слайдеры'
