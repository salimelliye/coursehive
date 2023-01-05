from django.forms import ModelForm 
from django import forms
from .models import *


class LinkRequestForm(ModelForm):
    Name = forms.TextInput()
    LastName = forms.TextInput()
    IDNumber = forms.NumberInput()
    Email = forms.EmailInput()
    class Meta:
        model = Student
        fields = ['Name', 'LastName', 'IDNumber', 'Email',]

      