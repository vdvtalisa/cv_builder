from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def register_page(request):
    if request.user.is_authenticated:
        return redirect('cv_view')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'cvapp/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'cvapp/register.html', {'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('cv_view')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'cvapp/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'cvapp/login.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('/')


def cv_form(request):
    personform = PersonForm(request.POST)
    contactform = ContactForm(request.POST)

    if personform.is_valid():
        personform.save()

    if contactform.is_valid():
        contactform.save()

    if personform.is_valid() & contactform.is_valid():
        return redirect('cv_view')

    context = {
        'personform': personform,
        'contactform': contactform
    }

    return render(request, 'cvapp/cv_form.html', context)


def cv_view(request):
    person = Person.objects.filter(user=request.user)
    contact_details = ContactDetails.objects.filter(person=request.user)
    # education = Education.objects.all()
    # work_experience = WorkExperience.objects.all()
    # skills = Skills.objects.all()
    # hobbies = Hobbies.objects.all()

    context = {'person': person,
               'contact_details': contact_details
               # 'education': education,
               # 'work_experience': work_experience,
               # 'skills': skills, 'hobbies': hobbies
               }

    return render(request, 'cvapp/cv_view.html', context)
