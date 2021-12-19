from rest_framework import serializers
from yearApp.models import year


class yearSerializer(serializers.ModelSerializer):
    class Meta:
        model = year
        fields = ('yid','y_name','mid')
