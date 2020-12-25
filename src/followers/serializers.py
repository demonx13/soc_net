from rest_framework import serializers
from .models import Follower
from ..profiler.serializers import UserByFollowerSerializer


class FollowerSerializer(serializers.ModelSerializer):
    """Return list of followers
    """
    user = UserByFollowerSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ("user",)
