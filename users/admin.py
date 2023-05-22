from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, playerProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(playerProfile)