import json
import jwt
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from engine.serializers import UserLoginSerializer, RefreshTokenSerializer


class GenerateTokensView(APIView):
    """
    API for token generation
    """
    permission_classes = ()

    response = None
    response_code = None

    def post(self, request):
        loginSerializer = UserLoginSerializer(data=request.data)
        if loginSerializer.is_valid():
            access_jwt = jwt.encode(
                {"email": loginSerializer.data['email']}, loginSerializer.data['secret'], algorithm="HS256")
            self.response = access_jwt
            self.response_code = 200
        else:
            self.response = loginSerializer.errors
            self.response_code = 400
        return Response(self.response, self.response_code)


class RefreshTokenView(APIView):
    """
    API for token refresh
    """
    permission_classes = ()

    response = None
    response_code = None

    def post(self, request):
        refreshTokenSerializer = RefreshTokenSerializer(data=request.data)
        if refreshTokenSerializer.is_valid():
            self.response = refreshTokenSerializer.data
        return Response(self.response, self.response_code)


