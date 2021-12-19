# -*- coding: utf-8 -*-
from django.db import models
from ratingApp.models import rating


# Create your models here.
class movie(models.Model):
    mid = models.IntegerField()
    title = models.CharField(max_length=4000)
    m_intro = models.CharField(max_length=4000)
    poster = models.CharField(max_length=4000)
'''

class movieAllInfo(models.Model):
    mid = models.ForeignKey(movie)
    title = models.ForeignKey(movie)
    m_intro = models.ForeignKey(movie)
    poster = models.ForeignKey(movie)
    rid = models.ForeignKey(rating)
    r_name = models.ForeignKey(rating)
'''