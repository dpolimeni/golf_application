from django.db.models.signals import post_save
from django.dispatch import receiver ## recieve the signal
from .models import CustomUser, playerProfile

@receiver(post_save, sender=CustomUser) #add this
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        playerProfile.objects.create(user=instance)
        
@receiver(post_save, sender=CustomUser) #add this
def save_user_profile(sender, instance, **kwargs):
    instance.playerprofile.save()