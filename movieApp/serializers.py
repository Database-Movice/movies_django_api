from rest_framework import serializers
from movieApp.models import movie



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ('mid','title','types','year',
                  'country','actor','director',
                  'm_intro','poster','rating')


