from django.db import models


class MinimalSetting(models.Model):
    name_site = models.CharField(
        verbose_name="Название сайта", max_length=150
    )
    description_site = models.CharField(
        verbose_name="Описание сайта", max_length=255, null=True, blank=True
    )
    keywords_site = models.TextField()
    phone_main = models.CharField(verbose_name="Телефон №1", max_length=18)
    phone_second = models.CharField(verbose_name="Телефон №2", max_length=18, null=True, blank=True)
    text_small_homepage_1 = models.CharField(
        verbose_name="Мини заголовок", max_length=80, null=True, blank=True)
    text_homepage_1 = models.CharField(verbose_name="Заголовок", max_length=80, null=True, blank=True)
    text_small_1 = models.CharField(verbose_name="Под заголовок", max_length=80, null=True, blank=True)
    facebook = models.CharField(verbose_name="Ссылка на facebook", max_length=255, null=True, blank=True)
    telegram = models.CharField(verbose_name="Ссылка на telegram", max_length=255, null=True, blank=True)
    twitter = models.CharField(verbose_name="Ссылка на twitter", max_length=255, null=True, blank=True)
    instagram = models.CharField(verbose_name="Ссылка на instagram", max_length=255, null=True, blank=True)
    tiktok = models.CharField(verbose_name="Ссылка на tiktok", max_length=255, null=True, blank=True)
    youtube = models.CharField(verbose_name="Ссылка на youtube", max_length=255, null=True, blank=True)
    vk = models.CharField(verbose_name="Ссылка на vk", max_length=255, null=True, blank=True)
    ok = models.CharField(verbose_name="Ссылка на odnoklassniki", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name_site
    
    class Meta:
        verbose_name_plural = "Настройки сайта"
        verbose_name = "настройка сайта"


class AboutContent(models.Model):
    big_img = models.ImageField(upload_to='about/', verbose_name="Большое фото")
    title = models.CharField(max_length=100)
    desc = models.TextField()
    autograph_img = models.ImageField(upload_to='about/', verbose_name="фото подписи")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'О нас'
        verbose_name = 'о нас'


class PlusAbout(models.Model):
    img = models.ImageField(upload_to='about/', verbose_name="фото")
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Плюсы компании'
        verbose_name = 'плюс компании'
        ordering = ['-id']


class BlogAbout(models.Model):
    img = models.ImageField(upload_to='about/', verbose_name="фото")
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Блог компании'
        verbose_name = 'блог компании'


class Faq(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Вопросы/Ответы'
        verbose_name = 'вопрос/ответ'


class Testimonials(models.Model):
    avatar = models.ImageField(upload_to='about/', verbose_name="фото")
    name = models.CharField(max_length=150, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="должность")
    desc = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'отзыв'