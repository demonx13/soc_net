from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Output private info about user"""

    avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class GetPublicUserNetSerializer(serializers.ModelSerializer):
    """Output public info about user"""
    class Meta:
        model = UserNet
        exclude = (
            "phone",
            "email",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "groups",
            'is_superuser',
            "user_permissions",
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """Followers serializer
    """
    avatar = serializers.ImageField(read_only=True, )

    class Meta:
        model = UserNet
        fields = ("id", "username", "avatar")
