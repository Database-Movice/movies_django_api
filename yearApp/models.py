from django.db import models


# Create your models here.
class year(models.Model):
    yid = models.IntegerField()
    y_name = models.CharField(max_length=4000)
    mid = models.IntegerField()


from django.db import models

# Create your models here.
