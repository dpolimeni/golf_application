from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.models import CustomUser
from django.views.generic import ListView, DetailView
from .models import Matches, MatchBooking

# Create your views here.
def create_match(request):
    return redirect('login-page')

@method_decorator(login_required, name='dispatch')
class match_list(ListView):
    model=Matches
    context_object_name = 'matches'
    ordering = ['-date']
    template_name = 'matches/match_list.html'
    
    #def get_ordering(self):
    #    ordering = self.request.GET.get('ordering', '-date_created')
    #    # validate ordering here
    #    return ordering    
    
class match_booking(DetailView):
    model = Matches
    template_name = 'matches/match_detail.html'
    
    def post(self, request, *args, **kwargs):
        form = self.request.POST
        match_id = self.kwargs['pk']
        partita = Matches.objects.get(pk=match_id)
        if partita.number_subscribed < partita.group_size:
            partita.number_subscribed += 1
            booking = MatchBooking(profile=self.request.user.playerprofile, match=partita)
            try:
                booking.save()
                partita.save()
            except Exception as e:
                print('ERROR :', e)
                return HttpResponse('TI SEI GIA PRENOTATO A QUESTA PARTITA')
            
            messages.success(request, f'Ti sei prenotato alla gara del {form["data"]} al circolo {partita.club.name}')           
            return redirect('profile-page')
        return HttpResponse('Work in progress')#render(request, self.template_name, {"form": form})