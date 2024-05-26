from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout

from doctor.models import Prescription
from .models import Patient

def register_patient(request):
    if request.method == 'POST':
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        email = request.POST.get('email')
        allergy = request.POST.get('allergy')
        phone = request.POST.get('phone')

        # Validate required fields
        if not all([lastname, firstname, gender, password, email, phone]):
            messages.error(request, 'Tous les champs obligatoires doivent être remplis.')
            return render(request, 'register_patient.html')
         # Hash the password
        password = make_password(password)
        try:
            # Validate email
            validate_email(email)
            
            # Create and save the patient instance
            patient = Patient(
                lastname=lastname,
                firstname=firstname,
                gender=gender,
                password=password,
                email=email,
                allergy=allergy,
                phone=phone
            )
            patient.save()
            
            messages.success(request, 'Successful registration ! Please log in.')
            return redirect('login_patient')  # Remplacez 'login_patient' par le nom de votre URL de connexion
        except ValidationError:
            messages.error(request, 'Invalid email address. Try Again.')
        except Exception as e:
            messages.error(request, f'Erreur : {str(e)}')

    return render(request, 'register_patient.html')

def login_patient(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            patient = Patient.objects.get(email=email)
            
            if check_password(password, patient.password):
                
                request.session['patient_id'] = patient.id  
                messages.success(request, 'Welcome patient '+ patient.lastname+' '+ patient.firstname+'!')
                return redirect('dashboard_patient')  
            else:
                messages.error(request, 'Incorrect password. Try Again.')
        except Patient.DoesNotExist:
            messages.error(request, 'No doctors found with this email address.')
        except Exception as e:
            messages.error(request, f'Erreur : {str(e)}')
    
    return render(request, 'login_patient.html')

def dashboard_patient(request):

    patient_id = request.session.get('patient_id')

    patient = Patient.objects.get(id=patient_id)
    prescriptions = Prescription.objects.filter(patient__id=patient_id)
    
    health_data = {
        "heart_rate": {
            "current": 72,  # BPM (beats per minute)
            "average_today": 68,
            "historical": [72, 70, 75, 65]
        },
        "blood_oxygen_level": {
            "current": 98,  # Percentage
            "average_today": 97
        },
        "physical_activity": {
            "steps_today": 4521,
            "distance_km": 3.5,  # Kilometers
            "floors_climbed": 10,
            "calories_burned": 345  # Calories
        },
        "sleep_tracking": {
            "duration_hours": 7.5,
            "sleep_phases": {
                "light": 4.5,  # Hours
                "deep": 2.0,
                "REM": 1.0
            }
        },
        "respiratory_rate": {
            "current": 14,  # Breaths per minute
            "average_today": 15
        },
        "stress_tracking": {
            "current_level": 20,  # Arbitrary scale, e.g., 0-100
            "average_today": 25
        }
    }

    context = {'health_data': health_data, 'patient': patient, 'prescriptions': prescriptions}
    return render(request, 'dashboard_patient.html', context)

def logout_patient(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login_patient')