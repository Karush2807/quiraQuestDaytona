from django import forms
from .models import Mudda
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MuddaForm(forms.ModelForm):
    class Meta:
        model=Mudda
        fields=['mudda_desc', 'mudda_img']

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2')