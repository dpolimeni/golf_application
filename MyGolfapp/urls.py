"""
URL configuration for GolfProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.views as auth_views
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home-first-screen'),
    path('register/', user_views.register, name='register-page'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout-page'),
    path('profile/', include('users.urls')),
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password-reset'),
    path('password_reset_confirm/<uidb64>/<token>', ## the psw reset calls an html that contains this url page with 2 params:
          auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), ## uidb64 and token
          name='password_reset_confirm'),
    path('password_reset/done/',
          auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
          name='password_reset_done'),
    path('password_reset_complete', 
          auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
          name='password_reset_complete'),
]

if settings.DEBUG: ## needed to add images on the site
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
