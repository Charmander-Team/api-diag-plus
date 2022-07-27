from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.ListUser.as_view()),
    path('', views.ListSpeciality.as_view()),
    path('<int:pk>/', views.DetailUser.as_view()),
]
