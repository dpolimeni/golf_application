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
import plotly.offline as opy
import plotly.graph_objs as go


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

def home_user(request):
    return render(request, 'users/base_user.html')

@login_required
def profile(request):
    data = [go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])]
    layout = go.Layout(title='Grafico Esempio')
    fig = go.Figure(data=data, layout=layout)
    
    # Convert the figure to HTML
    scatter_plot_div = opy.plot(fig, auto_open=False, output_type='div')
    
    data = [
        go.Bar(
            x=['Category A', 'Category B', 'Category C', 'Category D'],
            y=[10, 15, 7, 12]
        )
    ]
    layout = go.Layout(title='Bar Plot in Django')
    figure = go.Figure(data=data, layout=layout)
    bar_plot_div = opy.plot(figure, output_type='div')
    
    context = {'bar_plot': bar_plot_div, 'scatter_plot': scatter_plot_div}

    return render(request, 'users/profile.html', context)

@login_required
def profile_settings(request):
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
    return render(request, 'users/profile_settings.html', context)

@login_required
def other_profile(request, username):
    user = CustomUser.objects.get(username=username)
    if user.which_account == 'Gplayer':
        profile = user.playerprofile
    else:
        profile = user.clubprofile
    
    ### FAKE PLOTS
    data = [go.Scatter(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5])]
    layout = go.Layout(title=f'Statistiche di {username}')
    fig = go.Figure(data=data, layout=layout)
    
    scatter_plot_div = opy.plot(fig, auto_open=False, output_type='div')
    
    context = {
        'user':user,
        'scatter_plot':scatter_plot_div
    }
    return render(request, 'users/other_profile.html', context)