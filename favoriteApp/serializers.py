from rest_framework import serializers
from favoriteApp.models import favorite


class favoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = favorite
        fields = ('uid','mid')
