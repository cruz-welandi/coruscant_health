# Generated by Django 5.0.6 on 2024-05-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Pneumologie', 'Pneumologie'), ('Sports medicine', 'Sports medicine')], max_length=50),
        ),
    ]
