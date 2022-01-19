from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from Api import views
from Api.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()

# Api Routes
router.register(r'users', views.ListUser, 'user')
router.register(r'specialities', views.ListSpeciality,'speciality')
router.register(r'questions', views.ListQuestion, 'question')
router.register(r'attachements', views.ListAttachment, 'attachment')
router.register(r'patients', views.ListPatient, 'patient')
router.register(r'admin', views.ListAdmin, 'admin')
router.register(r'praticien', views.ListPraticien, 'praticien')
router.register(r'files', views.ListFiles, 'file')
router.register(r'report patient', views.ListReportPatient, 'report patient')
router.register(r'appointments', views.ListAppointment, 'appointment')
router.register(r'plannings', views.ListPlanning, 'planning')
router.register(r'diagnostics', views.ListDiagnostic, 'diagnostic')
router.register(r'responses', views.ListResponse, 'response')
router.register(r'pathologies', views.ListPathology, 'pathology')
router.register(r'reasons', views.ListReason, 'reason')
router.register(r'symptoms', views.ListSymptom, 'symptom')
router.register(r'admin/users', views.AdminUser, 'admin-user' )

# Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', GetTokenPair.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
