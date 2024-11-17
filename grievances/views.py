from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GrievanceForm
from .models import Grievance

@login_required
def grievance_list(request):
    if request.user.role == 'admin':
        grievances = Grievance.objects.all()
    else:
        grievances = Grievance.objects.filter(user=request.user)
    return render(request, 'grievances/grievance_list.html', {'grievances': grievances})

@login_required
def submit_grievance(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST, request.FILES)
        if form.is_valid():
            grievance = form.save(commit=False)
            grievance.user = request.user
            grievance.save()
            return redirect('grievance_list')
    else:
        form = GrievanceForm()
    return render(request, 'grievances/submit_grievance.html', {'form': form})
