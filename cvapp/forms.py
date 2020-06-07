from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['user', ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        exclude = ['user', ]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['user', ]
        widgets = {
            'start_date': forms.DateInput(format='%m/%d/%Y',
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
            'end_date': forms.DateInput(format='%m/%d/%Y',
                                        attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                               'type': 'date'}),
        }


class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['user', ]
        widgets = {
            'start_date': forms.DateInput(format='%m/%d/%Y',
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
            'end_date': forms.DateInput(format='%m/%d/%Y',
                                        attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                               'type': 'date'}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        exclude = ['user', ]


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobbies
        exclude = ['user', ]
