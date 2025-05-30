from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ProfilView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'username': str(request.user.username),  # `django.contrib.auth.User` instance.
            'email': str(request.user.email),  # `django.contrib.auth.User` instance.
            'password': str(request.user.password),  # `django.contrib.auth.User` instance.
            'is_authenticated': request.user.is_authenticated,  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)