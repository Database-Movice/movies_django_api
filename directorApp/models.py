from django.db import models


# Create your models here.
class director(models.Model):
    did = models.IntegerField()
    d_name = models.CharField(max_length=4000)
    mid = models.IntegerField()


from django.db import models

# Create your models here.
