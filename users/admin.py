from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "username"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
