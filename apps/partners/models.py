from django.db import models


class Partner(models.Model):
    name = models.CharField(verbose_name="Название", max_length=155)
    img = models.ImageField(upload_to='partners/', 
                            verbose_name="Лого партнера")
    link = models.CharField(
        max_length=255, verbose_name="Ссылка на партнера",
        help_text="Ссылка на их сайт или инстаграм или что-то"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="партнер"
        verbose_name_plural="Партнеры"