from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserAbstractSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(min_length=8)


class UserLoginSerializer(UserAbstractSerializer):
    pass


class UserRegisterSerializer(UserAbstractSerializer):

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError('Nickname already exists')
        return username
