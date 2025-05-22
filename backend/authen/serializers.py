from dj_rest_auth.serializers import LoginSerializer, PasswordResetSerializer
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField()
    # password2 = serializers.CharField()

    def validate(self, data):
        # if data['password1'] != data['password2']:
        #     raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email_or_username'])
            print('email', user)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=data['email_or_username'])
                print('username', user)
            except User.DoesNotExist:
                raise serializers.ValidationError("Not Found username or Email")
        user = authenticate(username=user.username, password=data["password"])
        # user = authenticate(username="anusornleo", password='12345678')
        print('user', user)
        if not user or not user.is_active:
            raise serializers.ValidationError("Invalid login")
        return {"user": user}

class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    # uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField()
