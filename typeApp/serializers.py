from rest_framework import serializers
from typeApp.models import type,onlyType


class typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = type
        fields = ('tid','t_name','mid')

class onltTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = onlyType
        field = ('t_name')