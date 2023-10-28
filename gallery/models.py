from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings


class Photo(models.Model):
    image_photo = models.ImageField(upload_to = 'images/')
    description  = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    photo = models.ForeignKey('gallery.Photo', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text