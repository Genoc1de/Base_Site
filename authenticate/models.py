from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])