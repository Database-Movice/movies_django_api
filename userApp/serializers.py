from rest_framework import serializers
from userApp.models import user


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('uid','uname','upwd')
