from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer, ResetPasswordRequestSerializer, ResetPasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"detail": "Please confirm your email."}, status=status.HTTP_201_CREATED)

class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "email": user.email,
            "username": user.username,
        })

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = RefreshToken.for_user(user)
        return Response({
            "access": str(token.access_token),
            "refresh": str(token),
        })

class ConfirmEmailView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # uid = force_str(urlsafe_base64_decode(request.GET.get("uid")))
        token = request.GET.get("token")
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"detail": "Email confirmed"})
        return Response({"detail": "Invalid token"}, status=400)

class RequestResetPasswordView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        user = User.objects.filter(email=request.data["email"]).first()
        if user:
            from .utils import send_password_reset_email
            send_password_reset_email(user)
        return Response({"detail": "If the email exists, a reset link has been sent."})

class ResetPasswordView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        # uid = force_str(urlsafe_base64_decode(request.data["uidb64"]))
        token = request.data["token"]
        new_password = request.data["new_password"]
        user = User.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password reset successful"})
        return Response({"detail": "Invalid token"}, status=400)
