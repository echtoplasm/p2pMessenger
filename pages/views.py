from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import Patient, Provider
# Create your views here.


# Create your views here.

class HomePageView(TemplateView):
  template_name = "home.html"

class LoginPageView(TemplateView):
  template_name = "login.html"

class MessagePageView(TemplateView):
  template_name = "messenger.html"




