from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, playerProfile, clubProfile
from django.forms import TextInput, NumberInput, ChoiceField, EmailInput

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
                }),
            'city': TextInput(attrs={
                'class': "form-control mb-3",
                #'style': 'max-width: 300px;',
                'placeholder': 'Città'
                }),
            'number_holes': forms.Select(attrs={
                'class': "select form-select",
                }),
            'experience': forms.Select(attrs={
                'class': "select form-select",
                }),
            'username': TextInput(attrs={
                'class': "form-control mb-3",
                #'style': 'max-width: 300px;',
                'placeholder': 'username'
                }),
            'email': EmailInput(attrs={
                'class': "emailinput form-control mb-3",
                #'style': 'max-width: 300px;',
                'placeholder': 'email',
                'required': True
                })
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'which_account']
        widgets = widgets
        
class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField(required=True, widget=widgets)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        widgets = widgets

class ProfileSignUpForm(forms.ModelForm):
    class Meta:
        model = playerProfile
        fields = ['name', 'surname']
        widgets = widgets

        
class ClubSignUpForm(forms.ModelForm):
    class Meta:
        model = clubProfile
        fields = ['name', 'city', 'number_holes']
        widgets = widgets

        
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = playerProfile
        fields = ['name', 'surname', 'experience', 'img']
        widgets = widgets
        
class ClubUpdateForm(forms.ModelForm):
    class Meta:
        model = clubProfile
        fields = ['img']