from rest_framework.generics import RetrieveAPIView
from django.shortcuts import render
from .serializers import GetUserNetSerializer
from .models import UserNet


# Create your views here.
class GetUserNetView(RetrieveAPIView):
    """Presentation info about user"""
    queryset = UserNet
    serializer_class = GetUserNetSerializer
