import requests
from .models import Profile
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from datetime import datetime




def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('sname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        Cpassword = request.POST.get('cpwd')

        if password == Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name= first_name,last_name=last_name,username=username, email=email,password=password)
                user.save()
                messages.info(request, "Account Created Successfully")
                return redirect('login')  # Redirect to login page
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('patient')  
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'registration/login.html')

def forgot(request):
    return render(request, 'forgot.html')

@login_required()
# Create your views here.



def user_logout(request):
    logout(request)
    return redirect('index')

#patient login
def patient_home(request):
    patient = User.objects.filter(patient=True).count()
    return render(request, 'patient/home.html')

def index(request):
    return render(request, 'index.html')

#CREATE PROFILE
def create_profile(request):
    if request.method == 'POST':
        username = request.user.username
        birth_date_str = request.POST.get('birth_date')  # Get birth date as a string
        gender = request.POST.get('gender')

        # Convert birth date string to a valid date object
        try:
            birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        except ValueError:
            birth_date = None  # Set birth date to None if the format is invalid

        # Create or update the profile
        profile, created = Profile.objects.update_or_create(
            user=request.user,
            defaults={'birth_date': birth_date, 'gender': gender}
        )

        messages.success(request, 'Profile Updated')
    
    else:
        profile = Profile.objects.filter(user=request.user).first()
        choice = ['1', '0']
        gender = ["Male", "Female"]
        context = {"profile": profile, "choice": choice, "gender": gender}
        return render(request, 'patient/create_profile.html', context)
    return redirect('patient')  # Redirect to the patient dashboard after updating the profile      


#def diagnosis():
#    symptoms = sorted(symptoms)
#    context = {'symptoms':symptoms, 'status':'1'}
#    return render(requests.request ,'patient/diagnosis.html',context)

