from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import GetUserNetSerializer, GetPublicUserNetSerializer
from .models import UserNet


class GetPubicUserNetView(ModelViewSet):
    """Public information about user
    """
    serializer_class = GetPublicUserNetSerializer
    permission_classes = [permissions.AllowAny]
    queryset = UserNet.objects.all()


class GetUserNetView(ModelViewSet):
    """Presentation info about user
    """

    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
