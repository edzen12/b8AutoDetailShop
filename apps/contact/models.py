from django.db import models


class ContactRequest(models.Model):
    name = models.CharField(max_length=150, verbose_name="ФИО")
    email = models.EmailField(verbose_name="Электронная почта")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name_plural = 'Форма обратной связи'
        verbose_name = 'форма связи'


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