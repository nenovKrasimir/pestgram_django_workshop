from django.db import models


# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=30)
    personal_photo = models.URLField()
    data_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True)