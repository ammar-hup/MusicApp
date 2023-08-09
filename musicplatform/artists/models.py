from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(blank = False,unique = True,max_length=200)
    socialLink = models.URLField(null=False)

    def __str__(self):
        return self.name    

    class Meta :
        ordering = ['name']
        verbose_name = "Artist"

