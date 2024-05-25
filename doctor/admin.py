from django.contrib import admin
from .models import Doctor, Prescription
from django import forms
from django.contrib.auth.hashers import make_password

class DoctorAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Doctor
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return make_password(password)
        return password
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'email', 'speciality', 'gender', 'creation_date']
    search_fields = ['lastname', 'firstname', 'speciality', 'gender']
    list_filter = ['gender', 'creation_date', 'speciality']
    list_editable = ['email', 'gender', 'speciality']
    
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.password = form.cleaned_data['password']
        super().save_model(request, obj, form, change)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['file', 'title', 'doctor', 'patient', 'date']
    search_fields = ['title', 'doctor', 'patient']
    list_filter = ['doctor', 'patient', 'date']
    list_editable = ['title']