from django.db import models


# Create your models here.
class Fish(models.Model):
        name = models.TextField()
        season = models.TextField()
