# Generated by Django 4.0 on 2022-07-26 09:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_user_alcohol_user_birthdate_user_gender_user_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+33123456789', max_length=128, region=None),
        ),
    ]