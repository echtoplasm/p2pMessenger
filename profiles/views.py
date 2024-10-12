from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from accounts.models import Patient, Provider


# Create your views here.
class ProviderProfileView(TemplateView):
  template_name = "provider_profile.html"

  def get_context_data(self, **kwargs):
    context = super(Provider).get_context_data(**kwargs)
    context['provider'] = Provider
    context['specialty'] = Provider.specialty
    context['first_name'] = Provider.first_name
    context['last_name'] = Provider.last_name
    context['medical_license_number'] = Provider.medical_license_number
    return context
  
class PatientProfileView(TemplateView):
  template_name = "patient_profile.html"

  def get_context_data(self, **kwargs):
    context = super(Patient).get_context_data(**kwargs)
    context['patient'] = Patient
    context['first_name'] = Patient.first_name
    context['last_name'] = Patient.last_name
    return context
    
    
  
  
  
