"""Models Creation"""
from email.policy import default
from pyexpat import model
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('Email address'), unique=True)
    first_name = models.CharField('First Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    telephone = PhoneNumberField(default='+33123456789')
    address = models.CharField('Address', max_length=255, default="Address")
    city = models.CharField('City', max_length=255, default="City")
    zipcode = models.CharField('Zipcode', max_length=5, default="00000")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    permission = models.PositiveIntegerField(
        default=1)  # Indique le rôle de l'utilisateur
    gender = models.CharField(max_length=50, default="Male")
    height = models.CharField(max_length=50, default=160)
    weight = models.CharField(max_length=50, default=70)
    origin = models.CharField(max_length=50, default="Origin")
    birthdate = models.DateField(default=timezone.now)
    smoking = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    role = models.CharField(max_length=255, default="Patient")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


class Question(models.Model):
    title = models.CharField('Title', max_length=255)
    type = models.CharField('Type', max_length=255)
    domain = models.PositiveIntegerField('Domain')


class Speciality(models.Model):
    name = models.CharField('Speciality', max_length=255)
    definition = models.CharField('Definition', max_length=255)


class Attachment(models.Model):
    id_type = models.PositiveIntegerField('Type')
    type = models.CharField('Type', max_length=255)
    name = models.CharField('Name', max_length=255)


class Files(models.Model):
    antecedent = models.CharField('Antecedent', max_length=255)
    allergy = models.CharField('Allergy', max_length=255)
    important_act = models.CharField('Important Act', max_length=255)
    organ_donation = models.CharField('Organ Donation', max_length=255)
    previous_medication = models.CharField(
        'Previous Medication', max_length=255)
    current_medication = models.CharField('Current Medication', max_length=255)


class ReportPatient(models.Model):
    type = models.CharField('Type', max_length=255)
    contenu = models.CharField('Content', max_length=255)
    attachment = models.ForeignKey(
        Attachment, on_delete=models.CASCADE, default=1)


class Appointment(models.Model):
    start_hour = models.DateTimeField()
    end_hour = models.DateTimeField()
    date = models.DateTimeField()
    reason = models.TextField('Reason')
    physical = models.BooleanField('Physical')


class Planning(models.Model):
    current_date = models.DateField()
    start_hours = models.DateTimeField()
    end_hours = models.DateTimeField()


class Diagnostic(models.Model):
    reason = models.CharField('Reason', max_length=255)
    pathology_bot = models.PositiveIntegerField()
    pathology_practicien = models.PositiveIntegerField()
    percentage = models.FloatField()


class Response(models.Model):
    response = models.TextField('Response')
    diagnostic = models.ForeignKey(
        Diagnostic, on_delete=models.CASCADE, default=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)


class Pathology(models.Model):
    name = models.CharField('Speciality', max_length=255)
    detail = models.CharField('Detail', max_length=255)
    practicien_speciality = models.CharField(
        'Practicien Speciality', max_length=255)
    speciality = models.ForeignKey(
        Speciality, on_delete=models.CASCADE, default=1)


class Reason(models.Model):
    name = models.CharField('Speciality', max_length=255)
    detail = models.CharField('Detail', max_length=255)
    pathologies = models.ForeignKey(
        Pathology, on_delete=models.CASCADE, default=1)


class Symptom(models.Model):
    name = models.CharField('Speciality', max_length=255)
    detail = models.CharField('Detail', max_length=255)
    pathologies = models.ForeignKey(
        Pathology, on_delete=models.CASCADE, default=1)


class Article(models.Model):
    title = models.CharField('Article', max_length=255)
    image = models.ImageField(upload_to='')
    description = models.TextField('Description')
    date = models.DateField()
