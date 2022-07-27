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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'address', 'city', 'zipcode', 'telephone',
                  'date_joined', 'birthdate', 'gender', 'height', 'weight', 'origin', 'smoking', 'alcohol', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.zipcode = validated_data.get('zipcode', instance.zipcode)
        instance.telephone = validated_data.get(
            'telephone', instance.telephone)
        instance.date_joined = validated_data.get(
            'date_joined', instance.date_joined)
        instance.birthdate = validated_data.get(
            'birthdate', instance.birthdate)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.height = validated_data.get('height', instance.height)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.origin = validated_data.get('origin', instance.origin)
        instance.smoking = validated_data.get('smoking', instance.smoking)
        instance.alcohol = validated_data.get('alcohol', instance.alcohol)
        instance.role = validated_data.get('role', instance.role)
        instance.set_password(instance.password)
        instance.save()
        return instance


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
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


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'antecedent',
            'allergy',
            'important_act',
            'organ_donation',
            'previous_medication',
            'current_medication',
        )
        model = Files


class ReportPatientSerializer(serializers.ModelSerializer):
    attachments = AttachementSerializer(many=False, read_only=False)

    class Meta:
        fields = (
            'type',
            'contenu',
            'attachments'
        )
        model = ReportPatient

    def create(self, validated_data):
        attachments_data = validated_data.pop('attachments')
        report_attachment = Attachment.objects.create(**validated_data)
        Attachment.objects.create(
            report_attachment=report_attachment, **attachments_data)
        return report_attachment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'start_hour',
            'end_hour',
            'date',
            'reason',
            'physical',
        )
        model = Appointment


class PlanningSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'current_date',
            'start_hours',
            'end_hours',
        )
        model = Planning


class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'reason',
            'pathology_bot',
            'pathology_practicien',
            'percentage',
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

    def create(self, validated_data):
        diagnostic_data = validated_data.pop('diagnostics')
        question_data = validated_data.pop('questions')
        response_question = Question.objects.create(**validated_data)
        response_diagnostic = Diagnostic.objects.create(**validated_data)
        Question.objects.create(
            response_question=response_question, **question_data)
        Diagnostic.objects.create(
            response_diagnostic=response_diagnostic, **diagnostic_data)
        return response_diagnostic, response_question


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
        pathology = Pathology.objects.create(**validated_data)
        Speciality.objects.create(pathology=pathology, **speciality_data)
        return pathology


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
        reason = Reason.objects.create(**validated_data)
        Pathology.objects.create(reason=reason, **pathology_data)
        return reason


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
        symptom = Symptom.objects.create(**validated_data)
        Pathology.objects.create(symptom=symptom, **pathology_data)
        return symptom


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'image',
            'description',
            'date'
        )
        model = Article
