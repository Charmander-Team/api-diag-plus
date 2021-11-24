from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .permissions import isAdminAuthenticated


class ListUser(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class AdminUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [isAdminAuthenticated] # Restrict the access to the admin only

    def get_queryset(self):
        return User.objects.all()
    
