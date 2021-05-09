""" Internal module for ease of managing JWT tokens """

# Native imports
import datetime
import base64
import json
import jwt

# Module imports
from rest_framework import serializers

# Application imports
from engine.models import User


class JWTHandler():

    token = None
    user = None

    secret = None
    payload = None

    def __init__(self, token=None, user=None):
        """ Bootstrapping parameters """
        if user:
            self.user = user
            self.__strap_user_secret()
            self.access = None
            self.refresh = None
        if token:
            print("poo")
            self.token = token
            self.__strap_token_payload()
            self.__strap_user_from_token()

    def __strap_token_payload(self):
        """ load the payload from token into state """
        try:
            jwt_payload = self.token.split('.')[1]
            self.payload = json.loads(base64.b64decode(
                jwt_payload + '=' * (-len(jwt_payload) % 4)).decode('ascii'))
        except Exception as exc:
            raise serializers.ValidationError(
                "Token parsing failed to parse payload") from exc

    def __strap_user_secret(self):
        """ Straps the user secret from user object stored in state """
        try:
            self.secret = self.user.retrieveSecret()
        except Exception as exc:
            raise serializers.ValidationError(
                "Error parsing user secret") from exc

    def __strap_user_from_token(self):
        """ straps the user object to state """
        try:
            self.user = User.objects.get(id=self.payload['uid'])
            self.__strap_user_secret()
        except Exception as exc:
            raise serializers.ValidationError(
                "Error loading user from token") from exc

    def validate_token(self):
        """ Method for validating token """
        is_valid = self.token is jwt.encode(
                json.loads(self.payload), self.secret, algorithm='HS256')
        return is_valid

    def get_tokens(self):
        """ Returns a new set of JWT token encoded with users private secret """
        try:
            if self.secret is not None and self.user is not None:

                # Generate new access token
                self.access = jwt.encode(
                    {
                        "email": self.user.email,
                        "uid": self.user.id,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
                    },
                    self.secret,
                    algorithm='HS256'
                )

                # Generate new refresh token
                self.refresh = jwt.encode(
                    {
                        "email": self.user.email,
                        "uid": self.user.id,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                    },
                    self.secret,
                    algorithm='HS256'
                )

        except Exception as exc:
            raise serializers.ValidationError(
                "Unable to generate new tokens") from exc

        # Only returns absolute token value only if it is generated successfully
        return {
            "access": self.access,
            "refresh": self.refresh
        }
