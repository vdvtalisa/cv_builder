from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def register_page(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    context = {'form': form}
    return render(request, 'cvapp/register.html', context)


def login_page(request):
    context = {}
    return render(request, 'registration/login.html', context)


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
    person = Person.objects.all()
    contact_details = ContactDetails.objects.all()
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
