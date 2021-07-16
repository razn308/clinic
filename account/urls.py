from django.urls import path
from .import  views

urlpatterns=[
    path('',views.index, name='index'),
    path('account/all_doctor',views.AllDoctor, name='all_doctor'),
    path('accounts/register/',views.register, name='register'),
    path('accounts/patient_register/',views.patient_register.as_view(), name='patient_register'),
    path('accounts/doctor_register/',views.doctor_register.as_view(), name='doctor_register'),
    path('accounts/login/',views.login_request, name='login'),
    path('accounts/logout/',views.logout_view, name='logout'),
]