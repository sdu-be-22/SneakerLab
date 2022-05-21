from dataclasses import field
from django import forms
from .models import * 

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
        fields = ["name", "surname", "email", "age", "cat", "stage", "content", "photo"]