from django.contrib import admin
from django.urls import path
import django.contrib.auth.views as auth_views
from users import views as user_views

urlpatterns = [
    path('home/', user_views.home_user, name='home-user'),
    path('', user_views.profile, name='profile-page'),
    path('settings/', user_views.profile_settings, name='profile-settings'),
    path('users/<str:username>', user_views.other_profile, name='other-profile')
]
