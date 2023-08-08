from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(blank = False,unique = True)
    socialLink = models.URLField(null=False)

    class Meta :
        ordering = ['name']
