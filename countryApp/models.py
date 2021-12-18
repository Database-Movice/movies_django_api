from django.db import models


# Create your models here.
class country(models.Model):
    cid = models.IntegerField()
    c_name = models.CharField(max_length=4000)
    mid = models.IntegerField()


from django.db import models

# Create your models here.
