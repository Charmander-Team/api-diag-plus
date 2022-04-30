from django import urls
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from Api import views
from Api.views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
router.register(r'articles', views.ListArticle, 'article')
router.register(r'admin/users', views.AdminUser, 'admin-user' )

# Patterns
# Need to add the https url in get_schema_view in order to be able to use the api doc
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Doc API for diagPlus",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alexandreto1996@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #url='https://api.diag-plus.tk/api/'
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', GetTokenPair.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

