from rest_framework import serializers
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        return authenticate(email=data.get('email', None), password=data.get('password', None))
