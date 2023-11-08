from django.shortcuts import render

from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class SignupView(APIView):
    serializer_class = serializers.SignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email').lower()
        user = serializer.save()

        user.username = email.split('@')[0]
        user.save()
        return Response({'status': True, 'message': 'user created successfully. Check your email for a verification code', 'data': serializer.data})


class GetUserView(APIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = self.serializer_class(request.user)
        return Response({"status": True, "message": "user retrieved successfully", "data": serializer.data})