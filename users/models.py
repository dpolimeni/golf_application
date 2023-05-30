from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.

class CustomUser(AbstractUser):
    OPTION_CHOICES = (
        ('Gplayer', 'Giocatore'),
        ('Gclub', 'Circolo'),
    )    

    which_account = models.CharField(max_length=20, choices=OPTION_CHOICES)

    def __str__(self) -> str:
        return super().__str__()


# Create your models here.
class playerProfile(models.Model):
    OPTION_EXPERIENCE = (
        ('< 1', '< 1'),
        ('1 - 3', '1 - 3'),
        ('> 3', ' > 3')
    ) 
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpeg', upload_to='image_pics')
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    experience = models.CharField(max_length=20, choices=OPTION_EXPERIENCE, default='-1')
    #description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):  ## rewrite save method to manage image dimensions
        super().save(*args, **kwargs)

        image = Image.open(self.img.path)

        if image.height > 300 or image.width > 300:  ## if we wecxceed max size we resize the image
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.img.path)

class clubProfile(models.Model):
    HOLES_CHOICES = (
        (9, 9),
        (18, 18)
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    number_holes = models.IntegerField(default=9, choices=HOLES_CHOICES)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=True, blank=True, default='Other')
    country = models.CharField(max_length=64, null=True, blank=True)
    address = models.TextField(default=None, blank=True, null=True)
    img = models.ImageField(default='default_club.jpeg', upload_to='image_pics')
    
    class Meta:
        ordering = ['name']
    
     

    
        