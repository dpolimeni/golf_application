from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, playerProfile, clubProfile
from django.forms import TextInput, NumberInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'which_account']
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

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
        
class ClubSignUpForm(forms.ModelForm):
    class Meta:
        model = clubProfile
        fields = ['name', 'country', 'number_holes']
        
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control mb-3",
                #'style': 'max-width: 300px;',
                'placeholder': 'Nome'
                }),
            'country': TextInput(attrs={
                'class': "form-control mb-3",
                #'style': 'max-width: 300px;',
                'placeholder': 'Nazione'
                }),
            'number_holes': NumberInput(attrs={
                'class': "form-control mb-3",
                })
        }
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = playerProfile
        fields = ['img']