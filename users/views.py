from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileSignUpForm, UserUpdateForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser


# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            register_form_data = dict(register_form.cleaned_data)
            username = register_form.cleaned_data.get('username')
            user = CustomUser.objects.get(username=username)
            profile_form = ProfileSignUpForm(request.POST, instance=user.playerprofile)
            if profile_form.is_valid():
                profile_form_data = dict(profile_form.cleaned_data)
                print(profile_form_data)
                profile_form.save()
            #username = register_form.cleaned_data.get('username')
            #messages.info(request, message=f"Account created for user {username}")
            print('form valido')
            print(register_form_data)
            return redirect('login-page') #HttpResponse('FORM VALIDO')
        print('form inviato ma non valido')
    else:
        register_form =UserRegisterForm()
        profile_form = ProfileSignUpForm()
    return render(request, "users/register.html", context={'register_form':register_form, 'profile_form': profile_form})

def home(request):
    return render(request, 'users/home.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #p_form
        if u_form.is_valid():
            u_form.save()
            messages.info(request, f'user {request.user.username} updated with succes')
    else:
        u_form = UserUpdateForm(instance = request.user)
        
    return render(request, 'users/profile.html', {'u_form':u_form})