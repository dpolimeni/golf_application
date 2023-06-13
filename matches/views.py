from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from django.views.generic import ListView
from .models import Matches

# Create your views here.
def create_match(request):
    return redirect('login-page')

class match_list(ListView):
    model=Matches
    context_object_name = 'matches'
    ordering = ['-date']
    template_name = 'users/home.html'
    
    #def get_ordering(self):
    #    ordering = self.request.GET.get('ordering', '-date_created')
    #    # validate ordering here
    #    return ordering    