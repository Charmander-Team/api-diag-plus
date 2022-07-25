from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Patient, Praticien


@receiver(post_save, sender=Patient)
@receiver(post_save, sender=Praticien)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


for user in User.objects.all():
    Token.objects.get_or_create(user=user)
