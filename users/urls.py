from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_views
from users import views as user_views
#from matches.views import match_list

urlpatterns = [
    path('home/', user_views.home_user, name='home-user'),
    path('', user_views.profile, name='profile-page'),
    path('settings/', user_views.profile_settings, name='profile-settings'),
    path('users/<str:username>', user_views.other_profile, name='other-profile'),
]
