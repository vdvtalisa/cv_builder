from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'title']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ['postcode', 'address', 'city', 'email', 'github', 'linkedin']
