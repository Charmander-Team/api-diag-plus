# Generated by Django 4.0 on 2022-07-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0008_admin_address_admin_city_admin_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='definition',
            field=models.CharField(max_length=255, verbose_name='Definition'),
        ),
    ]
