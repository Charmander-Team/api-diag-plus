from dataclasses import field
from rest_framework import serializers
from .models import *


class CommonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'telephone',
            'address',
            'city',
            'zipcode'
        )
        model: CommonInfo
        abstract = True


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
        model = Speciality


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'type',
            'domain'
        )
        model = Question


class AttachementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id_type',
            'type',
            'name'
        )
        model = Attachment


class PatientSerializer(CommonInfoSerializer):
    users = UserSerializer(many=False,  read_only=True)
    class Meta:
        fields = (
            'birth_date',
            'weight',
            'height',
            'origin',
            'smoker',
            'is_drinker',
            'users'
        )
        model = Patient
