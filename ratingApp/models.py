from django.db import models


# Create your models here.
class rating(models.Model):
    rid = models.IntegerField()
    r_name = models.CharField(max_length=4000)
    mid = models.IntegerField()


from django.db import models

# Create your models here.
