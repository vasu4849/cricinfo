from django.db import models
from django.urls import reverse


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='media', max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teams:team_detail', kwargs={'pk':self.pk})

