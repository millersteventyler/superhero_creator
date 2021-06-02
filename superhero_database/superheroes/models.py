from django.db import models


class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_superhero_ability = models.CharField(max_length=50)
    secondary_superhero_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)
# Create your models here.
