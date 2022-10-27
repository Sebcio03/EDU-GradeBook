from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from backend.users.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ["id", "email", "is_superuser"]
    search_fields = ["email"]
    ordering = ("email",)
