from dataclasses import field
from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject"]
        widgets = {
            'subject': forms.Textarea(attrs={'rows':10}),
        }


class VacancyForm(forms.ModelForm):

    class Meta:
        model = JobVacancies
        fields = ["name", "surname", "email", "age", "category", "stage", "content", "photo"]


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]