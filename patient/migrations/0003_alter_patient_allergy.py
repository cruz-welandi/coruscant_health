# Generated by Django 5.0.6 on 2024-05-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_rename_medical_history_patient_allergy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergy',
            field=models.CharField(choices=[('Pollen', 'Pollen'), ('Dust', 'Dust'), ('Mold', 'Mold')], max_length=50),
        ),
    ]
