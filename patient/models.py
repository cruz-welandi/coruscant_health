from django.contrib.auth.hashers import make_password
from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    creation_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128) 
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Patient(User):
    ALLERGY_CHOICES = [
        ('Pollen', 'Pollen'),
        ('Dust', 'Dust'),
        ('Mold', 'Mold'),
    ]
    allergy = models.CharField(max_length=50, choices= ALLERGY_CHOICES)