from django.db import models


# Create your models here.
class type(models.Model):
    tid = models.IntegerField()
    t_name = models.CharField(max_length=4000)
    mid = models.IntegerField()

class onlyType(models.Model):
    t_name= models.CharField(max_length=4000)

from django.db import models

# Create your models here.
