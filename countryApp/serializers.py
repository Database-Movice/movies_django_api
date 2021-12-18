from rest_framework import serializers
from countryApp.models import country


class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = ('cid','c_name','mid')
