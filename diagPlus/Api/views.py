from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
from rest_framework import viewsets
from .permissions import isAdminAuthenticated

# API Views
class ListUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes =[IsAuthenticatedOrReadOnly]

class ListSpeciality(viewsets.ModelViewSet):
    serializer_class = SpecialitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Speciality.objects.all()

    def has_permission(self, request, view):
        if request.user.is_authenticated: 
            return True
        return False

class ListQuestion(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class ListAttachment(viewsets.ReadOnlyModelViewSet):
    serializer_class = AttachementSerializer
    queryset = Attachment.objects.all()

class ListPatient(viewsets.ReadOnlyModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class ListAdmin(viewsets.ReadOnlyModelViewSet):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()

class ListPraticien(viewsets.ReadOnlyModelViewSet):
    serializer_class = PraticienSerializer
    queryset = Praticien.objects.all()

class ListFiles(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = Files.objects.all()

class ListReportPatient(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReportPatientSerializer
    queryset = ReportPatient.objects.all()

class AdminUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [isAdminAuthenticated] # Restrict the access to the admin only

    def get_queryset(self):
        return User.objects.all()
    
class GetTokenPair(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer