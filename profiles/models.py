from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import Patient, Provider
# Create your models here.

class PatientProfile(models.Model):
  user = models.OneToOneField(Patient, on_delete=models.CASCADE)
  bio = models.TextField(max_length=750, blank=True)
  medical_history = models.TextField(max_length=750, blank=True)
  profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

class ProviderProfile(models.Model):
  user = models.OneToOneField(Provider, on_delete=models.CASCADE)
  specialty = Provider.specialty
  bio = models.TextField(max_length=750, blank=True)
