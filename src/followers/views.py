from rest_framework import generics, permissions, views, response
from .serializers import FollowerSerializer
from .models import Follower
from ..profiler.models import UserNet


class ListFollowerView(generics.ListAPIView):
    """Show list of user followers
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(follower=self.request.user)


class FollowerView(views.APIView):
    """Add add follower for user
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

        try:
            user = UserNet.objects.get(id=pk)
        except UserNet.DoesNotExist:
            return response.Response(status=404)
        if request.user == user:
            return response.Response(status=404)
        if not Follower.objects.filter(user=user, follower=request.user):
            Follower.objects.create(follower=request.user, user=user)
            return response.Response(status=201)
        return response.Response(status=404)


    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(follower=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)
