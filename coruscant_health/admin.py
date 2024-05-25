# admin.py dans l'application patient
from django.contrib import admin
from patient.models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'email']

# admin.py dans l'application doctor
from django.contrib import admin
from doctor.models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'email']
