from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_patient , name='login_patient'),
    path('register', views.register_patient , name='register_patient'),
    path('dashboard', views.dashboard_patient , name='dashboard_patient'),
    path('logout/', views.logout_patient, name='logout_patient'),
]