import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes


class GenerateTokensView(APIView):
    """
    API for token generation
    """
    permission_classes = ()

    response = None
    response_code = None

    def post(self, request):
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
