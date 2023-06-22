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
    group_size = models.IntegerField(blank=True, default=4)
    number_subscribed = models.IntegerField(default=0) ## add check on less equal than the goup size
    club = models.ForeignKey(clubProfile, on_delete=models.CASCADE, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'club'], name='Unique datetime-Club for each match'
            ),
        ]
    
    
class MatchBooking(models.Model):
    profile = models.ForeignKey(playerProfile, on_delete=models.CASCADE)
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
     
    