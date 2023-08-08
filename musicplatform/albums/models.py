from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(default='New Album')
    creation_datetime = models.DateTimeField(auto_now_add=True)
    release_datetime = models.DateTimeField(blank=False, null=False)
    cost = models.FloatField(blank=False)