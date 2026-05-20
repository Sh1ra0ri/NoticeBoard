from django.conf import settings
from django.db import models
from django.db.models import ForeignKey

from ads.models import Ad


class Review(models.Model):
    text = models.TextField(verbose_name="Текст", help_text="Введите текст")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    ad = ForeignKey(Ad, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
