from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView

class LoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if not user:
            return Response(status=status.HTTP_403_FORBIDDEN,
                            data={'message': 'User data are wrong'})
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)
        return Response(data={'key': token.key})


class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response({"status": "Success!"}, status=status.HTTP_201_CREATED)


