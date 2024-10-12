from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Provider, Patient

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]

class ProviderAdmin(admin.ModelAdmin):
    model = Provider
    list_display = [
        'username',
        'email_address',
        'first_name',
        'last_name',
        "is_superuser",
    ]

class PatientAdmin(admin.ModelAdmin):
    model = Provider
    list_display = [
        'username',
        'email_address',
        'first_name',
        'last_name',
        "is_superuser",
    ]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Patient, PatientAdmin)
