from django import forms
from .models import Doctors, Specializaion


class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'


class SpecializaionForm(forms.ModelForm):
    class Meta:
        model = Specializaion
        fields = '__all__'
