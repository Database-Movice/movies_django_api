from rest_framework import serializers
from directorApp.models import director


class directorSerializer(serializers.ModelSerializer):
    class Meta:
        model = director
        fields = ('did','d_name','mid')
