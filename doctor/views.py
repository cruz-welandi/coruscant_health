from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from .models import Doctor, Prescription
from patient.models import Patient



# Create your views here.
def register_doctor(request):
    if request.method == 'POST':
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        email = request.POST.get('email')
        speciality = request.POST.get('speciality')
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
            doctor = Doctor(
                lastname=lastname,
                firstname=firstname,
                gender=gender,
                password=password,
                email=email,
                speciality=speciality,
                phone=phone
            )
            doctor.save()
            
            messages.success(request, 'Inscription réussie ! Veuillez vous connecter.')
            return redirect('login_doctor')  # Remplacez 'login_patient' par le nom de votre URL de connexion
        except ValidationError:
            messages.error(request, 'Adresse e-mail invalide. Veuillez réessayer.')
        except Exception as e:
            messages.error(request, f'Erreur : {str(e)}')
    return render(request, 'register_doctor.html')



def login_doctor(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            doctor = Doctor.objects.get(email=email)
            print(password, doctor.password)
            if check_password(password, doctor.password):
                # Mot de passe correct, connectez le médecin
                request.session['doctor_id'] = doctor.id  # Stocke l'ID du doctor dans la session
                messages.success(request, 'Connexion réussie !')
                return redirect('dashboard_doctor')  # Assurez-vous que 'dashboard_doctor' est défini dans vos URL
            else:
                messages.error(request, 'Mot de passe incorrect. Veuillez réessayer.')
        except Doctor.DoesNotExist:
            messages.error(request, 'Aucun médecin trouvé avec cette adresse e-mail.')
        except Exception as e:
            messages.error(request, f'Erreur : {str(e)}')
    
    return render(request, 'login_doctor.html')



def dashboard_doctor(request):
    patients = Patient.objects.all()
    doctor_id = request.session.get('doctor_id')
    prescriptions = Prescription.objects.filter(doctor__id=doctor_id)
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

    if doctor_id is not None:
        try:
            doctor = Doctor.objects.get(pk=doctor_id)
            # Vous pouvez maintenant utiliser l'objet 'doctor' dans votre template
            return render(request, 'dashboard_doctor.html', {'doctor': doctor, 'patients': patients, 'health_data': health_data, 'prescriptions': prescriptions})
        except Doctor.DoesNotExist:
            messages.error(request, 'Le médecin n\'existe pas.')
    else:
        messages.error(request, 'Veuillez vous connecter pour accéder à cette page.')
        return redirect('login_doctor')  # Redirige vers la page de connexion si l'ID du doctor n'est pas présent dans la session


def get_patient_details(request, patient_id):
    patient = Patient.objects.filter(id=patient_id).first()
    if patient:
        data = {
            'lastname': patient.lastname,
            'firstname': patient.firstname,
            'gender': patient.gender,
            'email': patient.email,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Patient not found'}, status=404)


def create_prescription(request, doctor_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        name_patient = request.POST.get('namePatient')
        file = request.FILES.get('file')

        try:
            patient = Patient.objects.get(lastname=name_patient)
            doctor = Doctor.objects.get(id=doctor_id)
            if patient and doctor:
                prescription = Prescription(title=title, patient=patient, file=file, doctor=doctor)
                prescription.save()
                messages.success(request, 'Prescription créée avec succès.')
                return redirect('dashboard_doctor')  # Assurez-vous que 'doctor_dashboard' est défini dans vos URL
            else:
                messages.error(request, 'Patient ou médecin introuvable.')
        except (Patient.DoesNotExist, Doctor.DoesNotExist):
            messages.error(request, 'Patient ou médecin introuvable.')
    
    return render(request, 'dashboard_doctor.html')