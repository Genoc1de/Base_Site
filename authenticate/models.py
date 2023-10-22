from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=100)
    date_posted = models.DateField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')