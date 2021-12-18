from rest_framework import serializers
from movieApp.models import movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ('mid', 'title','m_intro', 'poster')
