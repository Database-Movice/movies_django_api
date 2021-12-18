# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class movie(models.Model):
    mid = models.IntegerField()
    title = models.CharField(max_length=4000)
    m_intro = models.CharField(max_length=4000)
    poster = models.CharField(max_length=4000)
