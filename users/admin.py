from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, playerProfile, clubProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(playerProfile)
admin.site.register(clubProfile)