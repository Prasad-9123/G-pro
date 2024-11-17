from django.urls import path
from .views import grievance_list, submit_grievance

urlpatterns = [
    path('', grievance_list, name='grievance_list'),
    path('submit/', submit_grievance, name='submit_grievance'),
]
