from django.conf.urls.static import static
from django.urls import path
from coruscant_health import settings
from . import views

urlpatterns = [
    path('login', views.login_doctor , name='login_doctor'),
    path('register', views.register_doctor , name='register_doctor'),
    path('get-patient-details/<int:patient_id>/', views.get_patient_details, name='get-patient-details'),
    path('dashboard', views.dashboard_doctor , name='dashboard_doctor'),
    path('create-prescription/<int:doctor_id>/', views.create_prescription, name='create-prescription'),
    path('logout/', views.logout_doctor, name='logout_doctor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)