from django.conf import settings
from django.db import models


# Create your models here.
class Ad(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Название", help_text="Введите название"
    )
    price = models.IntegerField(verbose_name="Цена", help_text="")
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ad",
        verbose_name="Автор",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]
