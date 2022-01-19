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
    permission_classes = [IsAuthenticatedOrReadOnly]

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

class ListPatient(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Patient.objects.all()

class ListAdmin(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Admin.objects.all()

class ListPraticien(viewsets.ModelViewSet):
    serializer_class = PraticienSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Praticien.objects.all()

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

class AdminUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # Restrict the access to the admin only
    permission_classes = [isAdminAuthenticated]

    def get_queryset(self):
        return User.objects.all()
class GetTokenPair(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer
