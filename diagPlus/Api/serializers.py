from rest_framework import serializers
from .models import User, Speciality


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'email',
            'is_active',
            'date_joined',
        )
        model = User


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'definition'
        )
        model: Speciality
