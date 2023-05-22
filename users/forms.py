from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, playerProfile
from django.forms import TextInput

class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'which_account']

class ProfileSignUpForm(forms.ModelForm):
    class Meta:
        model = playerProfile
        fields = ['name', 'surname']
        
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control mb-3",
                #'style': 'max-width: 300px;',
                'placeholder': 'Nome'
                }),
            'surname': TextInput(attrs={
                'class': "form-control mb-3",
                #'style': 'max-width: 300px;',
                'placeholder': 'Cognome'
                })
        }