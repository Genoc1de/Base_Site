import self
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)  # Сохранение профиля

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image


class Element(models.Model):
    title = models.CharField(max_length=100, blank=True)
    text = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='element', blank=True)
