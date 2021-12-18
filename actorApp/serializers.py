from rest_framework import serializers
from actorApp.models import actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = ('aid', 'a_name','mid')
