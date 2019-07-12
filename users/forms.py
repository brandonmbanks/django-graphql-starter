from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class User:
        model = User
        fields = ("username", "email")