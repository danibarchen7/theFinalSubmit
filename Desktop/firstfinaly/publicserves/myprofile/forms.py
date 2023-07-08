from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyProfile


class SignupForm(UserCreationForm):
    class Meta:
        model = MyProfile
        fields = ['username', 'password1', 'password2', 'email', 'phone']
