from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from rest_framework import viewsets
from .permissions import isAdminAuthenticated


class ListUser(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ListSpeciality(viewsets.ReadOnlyModelViewSet):
    serializer_class = SpecialitySerializer
    queryset = Speciality.objects.all()

class ListQuestion(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class ListAttachment(viewsets.ReadOnlyModelViewSet):
    serializer_class = AttachementSerializer
    queryset = Attachment.objects.all()

class ListPatient(viewsets.ReadOnlyModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AdminUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [isAdminAuthenticated] # Restrict the access to the admin only

    def get_queryset(self):
        return User.objects.all()
    
