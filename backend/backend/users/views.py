from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from backend.users.models import User

from backend.users.serializers import UserSerializer, SignInSerializer, SignUpSerializer
from backend.users.throttle import SignUpThrottle

from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.contrib.auth import logout
from rest_framework import status

from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated


class GetCSRFToken(APIView):
    def get(self, request):
        return Response({"token": get_token(request)})


class SignUpAPIView(CreateAPIView):
    throttle_classes = [SignUpThrottle]
    serializer_class = SignUpSerializer
    queryset = User.objects.all()


class SignInAPIView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data["email"]
        password = serializer.data["password"]
        user = authenticate(request, username=email, password=password)

        if not user:
            raise ParseError("Invalid credentials")

        login(request, user)
        return Response()


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response()


class GetCurrentUserDataAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)
