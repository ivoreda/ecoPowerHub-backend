from django.shortcuts import render

from . import serializers
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

import random
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework import status



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


class ChangePasswordView(APIView):
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = get_object_or_404(User, id=request.user.id)

        try:
            user = User.objects.get(id=request.user.id)
        except Exception:
            raise AuthenticationFailed('user not found')
        if serializer.is_valid():

            old_password = serializer.data.get('old_password')
            new_password = serializer.data.get('new_password')

            if not user.check_password(old_password):
                return Response({"status": False, "message": "Old password is wrong"}, status=status.HTTP_400_BAD_REQUEST)
            if old_password == new_password:
                return Response({"status": False, "message": "New password must not be the same as old password"}, status=status.HTTP_400_BAD_REQUEST)

            if len(new_password) < 8:
                return Response({"status": False, "message": "New password must length must be greater than 8"}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()
            response = {
                "status": True,
                "message": "Password changed sucessfully"
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    serializer_class = serializers.ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email').lower()
            code = serializer.data.get('code')
            new_password = serializer.data.get('new_password')
            log = models.PasswordRecoveryLogs.objects.filter(
                email=email).first()
            if not log:
                return Response({"status": False, "message": "Password recovery logs not generated"})
            if log.email == email and log.code == code:
                user = models.CustomUser.objects.filter(email=email).first()
                user.set_password(new_password)
                user.save()
                log.isUsed = True
                log.save()
                return Response({"status": True, "message": "password reset successful"})
            elif log.email != email and log.code == code:
                return Response({"status": False, "message": "{email} does not match user".format(email=email)})
            elif log.email == email and log.code != code:
                return Response({"status": False, "message": "{code} does not match user code".format(code=code)})
            else:
                return Response({"status": False, "message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    serializer_class = serializers.ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email').lower()
            try:
                user = User.objects.get(email=email)
            except Exception:
                return Response({"status": False, "message": "User with this email {email} does not exist".format(email=email)})
            log = models.PasswordRecoveryLogs.objects.filter(
                email=email).first()
            if not log:
                code = generate_user_verification_code()
                user_password_recovery_log = models.PasswordRecoveryLogs.objects.create(
                    email=email, code=code)
                send_verification_code_to_email(
                    email, code, email_type='Password reset')
                return Response({"status": True, "message": "password reset code sent to {email}".format(email=email)})
            else:
                log.isUsed = False
                log.code = generate_user_verification_code()
                log.save()
                send_verification_code_to_email(
                    email, log.code, email_type='Password reset')
                return Response({"status": True, "message": "password reset code sent to {email}".format(email=email)})

class SendEmailVerificationCodeView(APIView):
    serializer_class = serializers.SendEmailVerificationCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_email = serializer.data.get('email').lower()
            user = models.CustomUser.objects.filter(email=user_email).first()
            if user is None:
                return Response({"status": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            if user.isVerified:
                return Response({"status": False, "message": "This user is already verified"})
            elif not user.isVerified:
                code = generate_user_verification_code()
                log = models.EmailVerificationLogs.objects.filter(
                    email=user_email).first()
                if log is None:
                    new_log = models.EmailVerificationLogs.objects.create(
                        email=user_email, code=code)
                    send_verification_code_to_email(
                        user_email, code, email_type='User verification')
                    return Response({"status": True, "message": f"Verification code sent to {user_email}"})
                else:
                    log.isUsed = False
                    log.code = generate_user_verification_code()
                    log.save()
                    send_verification_code_to_email(
                        user_email, log.code, email_type='User verification')
                    return Response({"status": True, "message": f"Verification code sent to {user_email}"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailVerificationView(APIView):
    serializer_class = serializers.VerifyEmailWithCodeSerializer

    def post(self, request):
        code = request.data.get('code')
        email = request.data.get('email').lower()
        log = models.EmailVerificationLogs.objects.filter(email=email).first()
        user = models.CustomUser.objects.filter(email=email).first()
        if log.isUsed == True and user.isVerified == True:
            return Response({"status": False, "message": "this code is already used and user is already verified"})
        if log.code == code and log.email == email:
            log.isUsed = True
            log.save()
            user.isVerified = True
            user.save()
            return Response({"status": True, "message": "User email verified successfully"})
        elif log.code != code and log.email == email:
            return Response({"status": False, "message": "Code is wrong"}, status=status.HTTP_400_BAD_REQUEST)
        elif log.code == code and log.email != email:
            return Response({"status": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"status": False, "message": "Something went wrong"})


def generate_user_verification_code():
    user_verification_code = random.randint(100000, 999999)
    return user_verification_code


def send_verification_code_to_email(user_email, user_code, email_type):
    subject = 'User Email Verification.'
    from_email = settings.EMAIL_HOST_USER

    from django.template.loader import render_to_string

    email_template = render_to_string(
        'registration/emails/verification_code_email.html', {'email': user_email, 'code': user_code, 'email_type': email_type})
    email_verification_email = EmailMessage(
        subject, email_template, from_email, [user_email]
    )
    email_verification_email.fail_silently = True
    email_verification_email.send()
