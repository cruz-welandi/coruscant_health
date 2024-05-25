from django.db import models
from patient.models import User, Patient

# Create your models here.
class Doctor(User):
    SPECIALITY_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Pneumologie', 'Pneumologie'),
        ('Sports medicine', 'Sports medicine'),
    ]
    speciality = models.CharField(max_length=50, choices=SPECIALITY_CHOICES)

def prescription_directory_path(instance, filename):
    return f'prescriptions/{filename}'

class Prescription(models.Model):
    title = models.CharField(max_length=200)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.FileField(upload_to=prescription_directory_path)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription {self.id} pour le patient {self.patient.lastname} par le docteur {self.doctor.lastname}"