from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Provider, Patient
from .forms import CustomUserCreationForm, ProviderForm, PatientForm
# Create your views here.

class ProfileView(View):
    def get(self, request):
        user_type = None
        if hasattr(request.user, 'patient'):
            user_type = Patient
            return render(request, 'patient_profile.html', {'user_type': user_type})
        elif hasattr(request.user, 'provider'):
            user_type = 'provider'
            return render(request, 'provider_profile.html', {'user_type': user_type})
        
class ProviderListView(View):
  def get(self, request):
    providers = Provider.objects.all()
    return render(request, 'providers_list.html', {'providers':providers})
  
class ProviderCreateView(View):
    def get(self, request):
        form = ProviderForm()
        return render(request, 'provider_form.html', {'form': form})

    def post(self, request):
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider = form.save()
            return redirect('provider_list')
        return render(request, 'provider_form.html', {'form': form})

class ProviderDetailView(View):
    def get(self, request, pk):
        provider = get_object_or_404(Provider, pk=pk)
        return render(request, 'provider_detail.html', {'provider': provider})

class ProviderUpdateView(View):
    def get(self, request, pk):
        provider = get_object_or_404(Provider, pk=pk)
        form = ProviderForm(instance=provider)
        return render(request, 'provider_form.html', {'form': form})

    def post(self, request, pk):
        provider = get_object_or_404(Provider, pk=pk)
        form = ProviderForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return redirect('provider_detail', pk=provider.pk)
        return render(request, 'provider_form.html', {'form': form})

# Patient Views
class PatientListView(View):
    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'patient_list.html', {'patients': patients})

class PatientCreateView(View):
    def get(self, request):
        form = PatientForm()
        return render(request, 'patient_form.html', {'form': form})

    def post(self, request):
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('patient_list')
        return render(request, 'patient_form.html', {'form': form})

class PatientDetailView(View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        return render(request, 'patient_detail.html', {'patient': patient})

class PatientUpdateView(View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientForm(instance=patient)
        return render(request, 'patient_form.html', {'form': form})

    def post(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', pk=patient.pk)
        return render(request, 'patient_form.html', {'form': form})

# User Registration View
class UserRegistrationView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to the login page after registration
        return render(request, 'registration/register.html', {'form': form})
