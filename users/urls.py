from django.urls import path

from .views import PasswordResetConfirmView, PasswordResetView, RegisterView

urlpatterns = [
    path("reset_password/", PasswordResetView.as_view()),
    path("reset_password_confirm/", PasswordResetConfirmView.as_view()),
    path("register/", RegisterView.as_view()),
]
