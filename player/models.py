from django.db import models

# Create your models here.
class Player(models.Model):
    won = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)
    ties = models.PositiveIntegerField(default=0)
    played = models.PositiveIntegerField(default=0)
