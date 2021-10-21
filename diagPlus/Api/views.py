from rest_framework import generics

from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets


class ListUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
