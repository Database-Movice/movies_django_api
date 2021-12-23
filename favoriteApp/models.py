from django.db import models

# Create your models here.
class favorite(models.Model):
    uid = models.IntegerField()
    mid = models.IntegerField()