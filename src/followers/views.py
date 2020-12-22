from rest_framework import generics, permissions, views, response
from .serializers import ListFollowerSerializer
from .models import Follower
from ..profiler.models import UserNet


class ListFollowerView(generics.ListAPIView):
    """Show list of user followers
    """
    permission_classes = [[permissions.IsAuthenticated]]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objecst.filter(user=self.request.user)


class AddFollowerView(views.APIView):
    """Add add follower for user
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = UserNet.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        return response.Response(status=404)
