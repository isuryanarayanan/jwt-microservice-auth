import json
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from engine.serializers import UserLoginSerializer


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
            self.response = loginSerializer.data
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

    def get(self, request):
        return Response(self.response, self.response_code)


class ValidateTokenView(APIView):
    """
    API for token validation
    """
    permission_classes = ()

    response = None
    response_code = None

    def get(self, request):
        return Response(self.response, self.response_code)
