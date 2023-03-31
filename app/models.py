from django.db import models

# Create your models here.
class Sports(models.Model):
    sports_name=models.CharField(max_length=100, primary_key=True)
class Players(models.Model):
    sports_name=models.ForeignKey(Sports, on_delete=models.CASCADE)
    players_name=models.CharField(max_length=100, unique=True)
    players_age=models.BigIntegerField()
class Address(models.Model):
    players_name=models.ForeignKey(Players, on_delete=models.CASCADE)
    players_state=models.CharField(max_length=100, unique=True)
    url=models.URLField()
            