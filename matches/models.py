from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from users.models import CustomUser, playerProfile, clubProfile
# Create your models here.


class Matches(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    