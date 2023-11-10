from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('me/', views.GetUserView.as_view(), name='me'),


    path('verify-email/', views.EmailVerificationView.as_view()),
    path('send-email-verification-code/', views.SendEmailVerificationCodeView.as_view(),
         name='send-email-verification-code'),
    path('forgot-password/', views.ForgotPasswordView.as_view()),
    path('reset-password/', views.ResetPasswordView.as_view()),
    path('change-password/', views.ChangePasswordView.as_view()),
]
