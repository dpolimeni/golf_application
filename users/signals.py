from django.db.models.signals import post_save
from django.dispatch import receiver ## recieve the signal
from .models import CustomUser, playerProfile, clubProfile

@receiver(post_save, sender=CustomUser) #add this
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.which_account == 'Gplayer':
            playerProfile.objects.create(user=instance)
        elif instance.which_account == 'Gclub':
            clubProfile.objects.create(user=instance)
        
@receiver(post_save, sender=CustomUser) #add this
def save_user_profile(sender, instance, **kwargs):
    if instance.which_account == 'Gplayer':
            instance.playerprofile.save()
    elif instance.which_account == 'Gclub':
            instance.clubprofile.save()
    