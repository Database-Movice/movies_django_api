from django.db import models

# Create your models here.
class actor(models.Model):
    aid = models.IntegerField()
    a_name = models.CharField(max_length=4000)
    mid = models.IntegerField()