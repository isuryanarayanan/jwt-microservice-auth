from rest_framework import serializers
from django.contrib.auth import authenticate
from engine.models import User, AuthSecret


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=250)
    password = serializers.CharField(max_length=128, write_only=True)
    secret = serializers.CharField(max_length=250, read_only=True)

    def validate(self, data):
        user = authenticate(email=data.get('email', None),
                            password=data.get('password', None))
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )

        try:
            user.generateNewSecret()
            user.save()
            jwt_token = user.retrieveSecret()
        except:
            print("error in generating user secret")

        return {
            'email': user.email,
            'secret': jwt_token
        }
