from django import forms

from .models import AdmissionApplication


class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ('first_name', 'last_name', 'email', 'phone', 'program')
