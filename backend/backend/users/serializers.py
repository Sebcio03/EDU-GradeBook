from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from backend.users.models import User


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class SignUpSerializer(serializers.ModelSerializer):
    agree_with_terms = serializers.BooleanField(write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "agree_with_terms"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_agree_with_terms(self, v):
        if not v:
            raise ValidationError("Terms have to be accepted")
        return v

    def create(self, validated_data):
        validated_data.pop("agree_with_terms")
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
