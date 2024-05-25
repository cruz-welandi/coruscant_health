from django.contrib import admin
from .models import Patient
from django import forms
from django.contrib.auth.hashers import make_password

class PatientAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Patient
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return make_password(password)
        return password


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'email', 'gender', 'allergy', 'creation_date']
    search_fields = ['lastname', 'firstname', 'allergy', 'gender']
    list_filter = ['gender', 'creation_date', 'allergy']
    list_editable = ['email', 'gender', 'allergy']

    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.password = form.cleaned_data['password']
        super().save_model(request, obj, form, change)

