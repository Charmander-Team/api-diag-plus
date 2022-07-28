from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
from rest_framework import viewsets
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser

# API Views


class ListUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ListSpeciality(viewsets.ModelViewSet):
    serializer_class = SpecialitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Speciality.objects.all()


class ListQuestion(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()


class ListAttachment(viewsets.ModelViewSet):
    serializer_class = AttachementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Attachment.objects.all()


class ListFiles(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Files.objects.all()


class ListReportPatient(viewsets.ModelViewSet):
    serializer_class = ReportPatientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ReportPatient.objects.all()


class ListAppointment(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Appointment.objects.all()


class ListPlanning(viewsets.ModelViewSet):
    serializer_class = PlanningSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Planning.objects.all()


class ListDiagnostic(viewsets.ModelViewSet):
    serializer_class = DiagnosticSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Diagnostic.objects.all()


class ListResponse(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Response.objects.all()


class ListPathology(viewsets.ModelViewSet):
    serializer_class = PathologySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Pathology.objects.all()


class ListReason(viewsets.ModelViewSet):
    serializer_class = ReasonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Reason.objects.all()


class ListSymptom(viewsets.ModelViewSet):
    serializer_class = SymptomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Symptom.objects.all()


class GetTokenPair(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer


class ListArticle(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
