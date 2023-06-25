from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, playerProfile, clubProfile, IronOwnership, Irons
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(playerProfile)
admin.site.register(clubProfile)
admin.site.register(Irons)
admin.site.register(IronOwnership)