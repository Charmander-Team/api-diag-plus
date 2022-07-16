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


class UserSerializer(CommonInfoSerializer):
    class Meta:
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'telephone',
            'address',
            'city',
            'zipcode',
            'is_active',
            'date_joined',
        )
        model = User

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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

    def create(self, validated_data):
        user_data = validated_data.pop('users')
        user = User.objects.create_user(**validated_data)
        User.objects.create(user=user, **user_data)
        return user


class AdminSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'users'
        )
        model = Admin

    def create(self, validated_data):
        user_data = validated_data.pop('users')
        user = User.objects.create_user(**validated_data)
        User.objects.create(user=user, **user_data)
        return user


class PraticienSerializer(CommonInfoSerializer):
    speciality = SpecialitySerializer(many=False, read_only=False)
    users = UserSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'speciality',
            'users'
        )
        model = Praticien

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        speciality_data = validated_data.pop('speciality')
        speciality = Speciality.objects.create(**validated_data)
        user = User.objects.create_user(**user_data)
        Speciality.objects.create(speciality=speciality, **speciality_data)
        User.objects.create(user=user, **user_data)
        return speciality, user


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

    def create(self, validated_data):
        patient_data = validated_data.pop('patients')
        patient = Patient.objects.create(**validated_data)
        Patient.objects.create(patient=patient, **patient_data)
        return patient


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

    def create(self, validated_data):
        patient_data = validated_data.pop('patients')
        attachments_data = validated_data.pop('attachments')
        patient = Patient.objects.create(**validated_data)
        attachment = Attachment.objects.create(**validated_data)
        Patient.objects.create(patient=patient, **patient_data)
        Attachment.objects.create(
            attachment=attachment, **attachments_data)
        return patient, attachment


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

    def create(self, validated_data):
        patient_data = validated_data.pop('patients')
        praticien_data = validated_data.pop('praticiens')
        patient = Patient.objects.create(**validated_data)
        praticien = Praticien.objects.create(**validated_data)
        Patient.objects.create(patient=patient, **patient_data)
        Praticien.objects.create(praticien=praticien, **praticien_data)
        return patient, praticien


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

    def create(self, validated_data):
        praticien_data = validated_data.pop('praticiens')
        praticien = Praticien.objects.create(**validated_data)
        Praticien.objects.create(praticien=praticien, **praticien_data)
        return praticien


class DiagnosticSerializer(serializers.ModelSerializer):
    praticiens = PraticienSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'reason',
            'pathology_bot',
            'pathology_practicien',
            'percentage',
            'patients',
            'praticiens'
        )
        model = Diagnostic

    def create(self, validated_data):
        praticien_data = validated_data.pop('praticiens')
        praticien = Praticien.objects.create(**validated_data)
        Praticien.objects.create(praticien=praticien, **praticien_data)
        return praticien


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

    def create(self, validated_data):
        diagnostic_data = validated_data.pop('diagnostics')
        question_data = validated_data.pop('questions')
        diagnostic = Diagnostic.objects.create(**validated_data)
        question = Question.objects.create(**validated_data)
        Question.objects.create(question=diagnostic, **question_data)
        Diagnostic.objects.create(diagnostic=diagnostic, **diagnostic_data)
        return diagnostic, question


class PathologySerializer(serializers.ModelSerializer):
    speciality = SpecialitySerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'name',
            'detail',
            'practicien_speciality',
            'speciality'
        )
        model = Pathology

    def create(self, validated_data):
        speciality_data = validated_data.pop('speciality')
        speciality = Speciality.objects.create(**validated_data)
        Speciality.objects.create(speciality=speciality, **speciality_data)
        return speciality


class ReasonSerializer(serializers.ModelSerializer):
    pathologies = PathologySerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'name',
            'detail',
            'pathologies'
        )
        model = Reason

    def create(self, validated_data):
        pathology_data = validated_data.pop('pathologies')
        pathology = Pathology.objects.create(**validated_data)
        Pathology.objects.create(pathology=pathology, **pathology_data)
        return pathology


class SymptomSerializer(serializers.ModelSerializer):
    pathologies = PathologySerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'name',
            'detail',
            'pathologies'
        )
        model = Symptom

    def create(self, validated_data):
        pathology_data = validated_data.pop('pathologies')
        pathology = Pathology.objects.create(**validated_data)
        Pathology.objects.create(pathology=pathology, **pathology_data)
        return pathology


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'image',
            'description',
            'date'
        )
        model = Article
