# Welcome to Coruscant Health Administration
***

## Task
Coruscant Health Administration is a hospital management project where our tasks are:

  ****patient side*****

1. patients can register and log in to their dashboard
2. they can access their information from connected watches
3. they can download prescriptions issued by doctors

****doctor side*****

1. the doctor can register and connect to his dashboard
2. he sees patient information in order to make prescriptions
3. he can make prescriptions to patients therefore upload a document.

****admin side*****

1. the admin has seen everything, he can register a patient and a doctor
2. he can modify the information of patients and doctors, of a prescription
3. it can delete a doctor, a patient and a prescription
4.he can also make prescriptions 
In all, the admin is in charge of everything.

## Description
For this project, when the patient and the doctor arrive on the home page, they will make a choice between doctor or patient after this will be sent to a login page to log in if they already have an account otherwise they will first have to register then log in and everyone is directed to their respective dashboard.

****dashboard patient*****
1. Patient can download doctor's prescriptions,
2. view the information of this connected watch
3. he can also disconnect

*****doctor dashboard*****
1. It can see patients' smart watch information,
2. he can upload the document to create a prescription with a title and the name of the patient concerned
3. he can disconnect

****dashboard administrator*****
to access the dashboard you need to click on this link https://welandicruz.pythonanywhere.com/admin

`username: admin`
`password: admin`

## Installation

For this project we used a virtual environment. 
to create a virtual environment you must type this command 
`python -m venv env`
env represents the name of your virtual environment
to activate this environment you do this command

Under Windows
`env\Scripts\activate`

Under macOS and Linux
`source env/bin/activate`

once the environment is created you can now install django with this command:
`pip install django`

then you type for django project
```
django-admin startproject coruscant_health
cd coruscant_health
```
to start the server 
```
python manage.py runserver
```
we created two applications in our doctor and patient projects with these commands
```
python manage.py startapp patient
python manage.py startapp doctor
```

## Usage
to see the project we invite you to click on this link 
https://welandicruz.pythonanywhere.com

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>