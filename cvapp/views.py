from django.contrib.auth.decorators import login_required
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
    personform = PersonForm()
    contactform = ContactForm()
    educationform = EducationForm()
    workform = WorkForm()
    skillform = SkillForm()
    hobbyform = HobbyForm()
    if request.method == 'POST':
        personform = PersonForm(request.POST)
        contactform = ContactForm(request.POST)
        educationform = EducationForm(request.POST)
        workform = WorkForm(request.POST)
        skillform = SkillForm(request.POST)
        hobbyform = HobbyForm(request.POST)

        if personform.is_valid():
            form = personform.save()
            form.user = request.user
            form.save()

        if contactform.is_valid():
            form = contactform.save()
            form.user = request.user
            form.save()

        if educationform.is_valid():
            form = educationform.save()
            form.user = request.user
            form.save()

        if workform.is_valid():
            form = workform.save()
            form.user = request.user
            form.save()

        if skillform.is_valid():
            form = skillform.save()
            form.user = request.user
            form.save()

        if hobbyform.is_valid():
            form = hobbyform.save()
            form.user = request.user
            form.save()

        if personform.is_valid() & contactform.is_valid() & educationform.is_valid() & workform.is_valid() & skillform.is_valid() & hobbyform.is_valid():
            return redirect('cv_view')

    context = {
        'personform': personform,
        'contactform': contactform,
        'educationform': educationform,
        'workform': workform,
        'skillform': skillform,
        'hobbyform': hobbyform
    }

    return render(request, 'cvapp/cv_form.html', context)


@login_required
def cv_view(request):
    person = Person.objects.filter(user=request.user).latest('pk')
    contact_details = ContactDetails.objects.filter(user=request.user).latest('pk')
    education = Education.objects.filter(user=request.user)
    work = WorkExperience.objects.filter(user=request.user)
    skills = Skills.objects.filter(user=request.user)
    hobbies = Hobbies.objects.filter(user=request.user)

    context = {'person': person,
               'contact_details': contact_details,
               'education': education,
               'work': work,
               'skills': skills,
               'hobbies': hobbies
               }

    return render(request, 'cvapp/cv_view.html', context)
