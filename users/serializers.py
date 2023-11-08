from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ["first_name", "last_name", "email",
                "phone_number", "user_type", "profile_picture", "business_worth",
                "business_description", "available_shares", "total_shares",
                "buyable_shares", "buyable_shares_percentage", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("User with email already exists")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user_type = validated_data.pop('user_type', None)

        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        if user_type is not None and user_type not in ['User', 'Business']:
            raise serializers.ValidationError({'status': False, 'message': 'user_type should be either User or Business'})
        instance.user_type = user_type
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        exclude = ['password']