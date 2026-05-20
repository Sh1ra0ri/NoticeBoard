from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()
    username = None
    first_name = models.CharField(
        max_length=100, help_text="Введите ваше имя", verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=100, help_text="Введите вашу фамилию", verbose_name="Фамилия"
    )
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите вашу почту", blank=False
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
    )

    image = models.ImageField(
        upload_to="users/avatars",
        null=True,
        blank=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    class UserRoles(models.TextChoices):
        USER = "user", "Пользователь"
        ADMIN = "admin", "Администратор"

    role = models.CharField(
        max_length=10,
        choices=UserRoles.choices,
        default=UserRoles.USER,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
