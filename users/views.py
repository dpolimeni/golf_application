from django.shortcuts import render, redirect
from .forms import (UserRegisterForm,
                    ProfileSignUpForm,
                    UserUpdateForm, 
                    ProfileUpdateForm,
                    ClubSignUpForm
                    )
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from .utils import form_generator


# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            register_form_data = dict(register_form.cleaned_data)
            if register_form_data['which_account'] == 'Gplayer':
                username = register_form.cleaned_data.get('username')
                user = CustomUser.objects.get(username=username)
                profile_form = ProfileSignUpForm(request.POST, instance=user.playerprofile)
                if profile_form.is_valid():
                    profile_form_data = dict(profile_form.cleaned_data)
                    print(profile_form_data)
                    profile_form.save()
            if register_form_data['which_account'] == 'Gclub':
                username = register_form.cleaned_data.get('username')
                user = CustomUser.objects.get(username=username)
                club_form = ClubSignUpForm(request.POST, instance=user.clubprofile)
                if club_form.is_valid():
                    club_form_data = dict(club_form.cleaned_data)
                    print(club_form_data)
                    club_form.save()
           
                print('form valido')
                print(register_form_data)
            return redirect('login-page') #HttpResponse('FORM VALIDO')
        print('form inviato ma non valido')
    else:
        register_form =UserRegisterForm()
        profile_form = ProfileSignUpForm()
        club_form = ClubSignUpForm()
    return render(request, "users/register.html", context={'register_form':register_form,
                                                           'profile_form': profile_form,
                                                           'club_form':club_form})

def home(request):
    return render(request, 'users/home.html')

@login_required
def profile(request):
    u_form, p_form = form_generator(request, request.user.which_account)
    if request.method == 'POST':
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, f'user {request.user.username} updated with succes')
            return redirect('profile-page')
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)