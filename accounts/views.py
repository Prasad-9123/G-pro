from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'  
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')  
        else:
            print("Form Errors:", form.errors)
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Grievance
from .forms import GrievanceForm, UserProfileForm

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        grievances = Grievance.objects.all()
    else:
        grievances = Grievance.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', {'grievances': grievances})

@login_required
def create_grievance(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            grievance = form.save(commit=False)
            grievance.user = request.user
            grievance.save()
            return redirect('dashboard')
    else:
        form = GrievanceForm()
    return render(request, 'accounts/create_grievance.html', {'form': form})

@login_required
def edit_grievance(request, grievance_id):
    grievance = get_object_or_404(Grievance, id=grievance_id)
    if request.user.role != 'admin' and grievance.user != request.user:
        return redirect('dashboard')
    if request.method == 'POST':
        form = GrievanceForm(request.POST, instance=grievance)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GrievanceForm(instance=grievance)
    return render(request, 'accounts/edit_grievance.html', {'form': form})
