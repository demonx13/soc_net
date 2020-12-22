from rest_framework import serializers
from ..profiler.models import UserNet
from .models import Follower
from ..profiler.serializers import UserByFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):
    """Return list of followers
    """
    follower = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ("follower",)

