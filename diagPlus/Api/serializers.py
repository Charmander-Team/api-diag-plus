from dataclasses import field
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Claim Token
class TokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(TokenPairSerializer, cls).get_token(user)

        token['email'] = user.email
        return token


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


class AdminSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'users'
        )
        model = Admin


class PraticienSerializer(CommonInfoSerializer):
    speciality = SpecialitySerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'speciality'
        )
        model = Praticien


class FileSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'antecedent',
            'allergy',
            'important_act',
            'organ_donation',
            'previous_medication',
            'current_medication',
            'patients'
        )
        model = Files


class ReportPatientSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=False, read_only=False)
    attachments = AttachementSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'type',
            'contenu',
            'patients',
            'attachments'
        )
        model = ReportPatient


class AppointmentSerializer(serializers.ModelSerializer):
    patients = PatientSerializer(many=False, read_only=False)
    praticiens = PraticienSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'start_hour',
            'end_hour',
            'date',
            'reason',
            'physical',
            'patients',
            'praticiens'
        )
        model = Appointment

class PlanningSerializer(serializers.ModelSerializer):
    praticiens = PraticienSerializer(many=False, read_only=False)
    
    class Meta:
        fields = (
            'current_date',
            'start_hours',
            'end_hours',
            'praticiens'
        )
        model = Planning

class DiagnosticSerializer(serializers.ModelSerializer):
    praticiens = PraticienSerializer(many=False, read_only=False)

    class Meta: 
        fields = (
            'reason',
            'pathology_bot',
            'pathology_praticien',
            'percentage',
            'patients',
            'praticiens'
        )
        model = Diagnostic

class ResponseSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=False, read_only=False)
    diagnostics = DiagnosticSerializer(many=False, read_only=False) 
    class Meta: 
        fields = (
            'response',
            'diagnostics',
            'questions'
        )
        model = Response

class PathologySerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer(many=False, read_only=False)

    class Meta: 
        fields = (
            'name',
            'detail',
            'praticien_speciality',
            'speciality'
        )
        model = Pathology

class ReasonSerializer(serializers.ModelSerializer):
    pathologies = PathologySerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'name',
            'detail',
            'pathologies'
        )
        model = Reason

class SymptomSerializer(serializers.ModelSerializer):
    pathologies = PathologySerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'name',
            'detail',
            'pathologies'
        )
        model = Symptom