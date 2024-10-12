from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Provider, Patient
from django import forms

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = (
      "email",
      "username",
    )

class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = get_user_model()
    fields = (
      "email",
      "username",
    )

class ProviderCreationForm(forms.ModelForm):
  class Meta:
    model = Provider
    fields = (
      "first_name",
      "last_name",
      "phone_number",
      "email_address",
      "specialty",
    )

class ProviderUserChangeForm(forms.ModelForm):
  class Meta:
    model = Provider
    fields = (
      "first_name",
      "last_name",
      "phone_number",
      "email_address",
      "specialty",
    )

class PatientUserCreationForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = (
      "first_name",
      "last_name",
      "email_address",
      "ssn",
      "insurance_policy",
      "provider",

    )

class PatientUserChangeForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = (
      "first_name",
      "last_name",
      "email_address",
      "ssn",
      "insurance_policy",
      "provider",
    )
