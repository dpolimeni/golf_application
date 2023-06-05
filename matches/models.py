from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from users.models import CustomUser, playerProfile, clubProfile
# Create your models here.


class Matches(models.Model):
    match_types = (
        ('Unofficial', 'Amatoriale'),
        ('Official', 'Ufficiale')
    )
    date = models.DateTimeField(auto_now_add=False)
    type = models.CharField(max_length=32, choices=match_types, null=True, blank=True)
    group_size = models.IntegerField(null=True, blank=True)
    
    