from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Grievance, CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  
        fields = ['role','username', 'email', 'password1', 'password2']  

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['title', 'description', 'status']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
