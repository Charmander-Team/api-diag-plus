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
        model = CommonInfo
        abstract = True


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


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Patient

    def create(self, validated_data):
        return Patient.objects.create_user(**validated_data)


class AdminSerializer(CommonInfoSerializer):

    class Meta:
        fields = '__all__'
        model = Admin


class PraticienSerializer(CommonInfoSerializer):
    speciality = SpecialitySerializer(read_only=True, many=False)

    class Meta:
        fields = '__all__'
        model = Praticien

    def create(self, validated_data):
        speciality_data = validated_data.pop('speciality')
        praticien = Praticien.objects.create_user(**validated_data)
        Speciality.objects.create(praticien=praticien, **speciality_data)
        return praticien


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
        file = Files.objects.create(**validated_data)
        Patient.objects.create(file=file, **patient_data)
        return file


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
        report_patient = Patient.objects.create(**validated_data)
        report_attachment = Attachment.objects.create(**validated_data)
        Patient.objects.create(report_patient=report_patient, **patient_data)
        Attachment.objects.create(
            report_attachment=report_attachment, **attachments_data)
        return report_patient, report_attachment


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
        appointment_patient = Patient.objects.create(**validated_data)
        appointment_practicien = Praticien.objects.create(**validated_data)
        Patient.objects.create(
            appointment_patient=appointment_patient, **patient_data)
        Praticien.objects.create(
            appointment_practicien=appointment_practicien, **praticien_data)
        return appointment_patient, appointment_practicien


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
        planning = Planning.objects.create(**validated_data)
        Praticien.objects.create(planning=planning, **praticien_data)
        return planning


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
        diagnostic = Diagnostic.objects.create(**validated_data)
        Praticien.objects.create(diagnostic=diagnostic, **praticien_data)
        return diagnostic


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
