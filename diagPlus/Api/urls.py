from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListSpeciality.as_view()),
    path('<int:pk>/', views.DetailUser.as_view()),
]
