from django.urls import path
from .views import CustomLoginView, register,dashboard,create_grievance,edit_grievance

urlpatterns = [
    path('register/', register, name='register'),
     path('login/', CustomLoginView.as_view(), name='login'),
     path('dashboard/', dashboard, name='dashboard'),
    path('grievance/create/', create_grievance, name='create_grievance'),
    path('grievance/edit/<int:grievance_id>/', edit_grievance, name='edit_grievance'),
]
