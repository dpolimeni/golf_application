from django.db.models.signals import post_save
from django.dispatch import receiver ## recieve the signal
from .models import CustomUser, playerProfile

@receiver(post_save, sender=CustomUser) #add this
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.which_account == 'Gplayer':
            playerProfile.objects.create(user=instance)
        elif instance.which_account == 'Gclub':
            pass
        
@receiver(post_save, sender=CustomUser) #add this
def save_user_profile(sender, instance, **kwargs):
    if instance.which_account == 'Gplayer':
            instance.playerprofile.save()
    elif instance.which_account == 'Gclub':
            pass
    