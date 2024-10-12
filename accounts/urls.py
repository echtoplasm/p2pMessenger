from django.urls import path
from .views import (ProviderDetailView, PatientDetailView, ProviderUpdateView, PatientUpdateView, ProviderListView, PatientListView, ProfileView)

urlpatterns = [
  path("<uuid:pk>/", PatientDetailView.as_view(), name="patient_page"),
  path("<uuid:pk>/", ProviderDetailView.as_view(), name="provider_page"),
  path("provider_update/", ProviderUpdateView.as_view(), name="provider_update"),
  path("patient_update/", PatientUpdateView.as_view(), name="patient_update"),
  path("patient_list/", ProviderListView.as_view(), name="provider_list"),
  path("patient_list/", PatientListView.as_view(), name="patient_list"),
  path("profile/", ProfileView.as_view(), name="profiles",)
]
