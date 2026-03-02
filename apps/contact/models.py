from django.db import models


class ContactInfo(models.Model):
    map = models.TextField(
        verbose_name="Карта",
        help_text="iframe вставляем из источников"
    )
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Контакты"
        verbose_name = 'контакт'