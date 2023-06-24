from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_views
from users import views as user_views
from matches.views import match_list, match_booking

urlpatterns = [
    path('match_list', match_list.as_view(), name='match-list'),
    path('match/<int:pk>', match_booking.as_view(), name='match-detail')
]
