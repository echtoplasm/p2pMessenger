from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

# Create your models here.

class CustomUser(AbstractUser):
  pass


class Provider(AbstractUser):
  id = models.UUIDField(
    primary_key=True, 
    default=uuid.uuid4,
    editable=False
  )
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=15)
  email_address = models.CharField(max_length=100)
  specialty = models.CharField(max_length=100)
  medical_license_number = models.CharField(max_length=20, default='ME0000')
  last_login = models.DateTimeField(null=True, blank=True)


  groups = models.ManyToManyField(
    Group,
    related_name='providers',
    blank=True,
  )

  user_permissions = models.ManyToManyField(
    Permission,
    related_name='providers',
    blank=True,
  )


  class Meta:
    verbose_name = "Providers"
    verbose_name_plural = "Providers"

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  


  

class Patient(AbstractUser):
  id = models.UUIDField(
    primary_key=True, 
    default=uuid.uuid4,
    editable=False
  )
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=15)
  email_address = models.CharField(max_length=100)
  last_login = models.DateTimeField(null=True, blank=True)
  insurance_policy = models.CharField(max_length=128)
  ssn = models.CharField(max_length=15)
  provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="patients", null=True, blank=True)


  groups = models.ManyToManyField(
    Group,
    related_name='patients',
    blank=True,
  )

  user_permissions = models.ManyToManyField(
    Permission,
    related_name='patients',
    blank=True,
  )

  class Meta:
    verbose_name = "Patient"
    verbose_name_plural = "Patients"

  def __str__(self):
    return f"{self.first_name} {self.last_name}"
