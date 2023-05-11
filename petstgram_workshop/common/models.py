from django.db import models

from petstgram_workshop.photos.models import Photo


# Create your models here.


class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
