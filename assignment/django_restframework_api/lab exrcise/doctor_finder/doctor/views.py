from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Doctor

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/doctors/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/doctors/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def doctor_list(request):
    if request.user.is_superuser:
        doctors = Doctor.objects.all()
    else:
        doctors = Doctor.objects.filter(user=request.user)
    return render(request, 'doctor_list.html', {'doctors': doctors})

@login_required(login_url='/login/')
def add_doctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        specialty = request.POST['specialty']
        phone = request.POST['phone']
        email = request.POST['email']
        image = request.FILES.get('image')
        Doctor.objects.create(
            user=request.user,
            name=name,
            specialty=specialty,
            phone=phone,
            email=email,
            image=image
        )
        return redirect('/doctors/')
    return render(request, 'add_doctor.html')

@login_required(login_url='/login/')
def update_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doctor.name = request.POST['name']
        doctor.specialty = request.POST['specialty']
        doctor.phone = request.POST['phone']
        doctor.email = request.POST['email']
        if request.FILES.get('image'):
            doctor.image = request.FILES['image']
        doctor.save()
        return redirect('/doctors/')
    return render(request, 'update_doctor.html', {'doctor': doctor})

@login_required(login_url='/login/')
def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('/doctors/')