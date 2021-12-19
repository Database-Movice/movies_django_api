from rest_framework import serializers
from ratingApp.models import rating
from movieApp.models import movie

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = rating
        fields = ('rid','r_name','mid')



class totalRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = rating
        fields = ('rid','r_name','mid')
