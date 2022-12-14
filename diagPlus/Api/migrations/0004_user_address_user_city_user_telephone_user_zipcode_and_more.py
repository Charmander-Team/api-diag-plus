# Generated by Django 4.0 on 2022-07-16 15:58

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Address', max_length=255, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='City', max_length=255, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='zipcode',
            field=models.CharField(default='00000', max_length=5, verbose_name='Zipcode'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(default='Address', max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(default='City', max_length=255, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='zipcode',
            field=models.CharField(default='00000', max_length=5, verbose_name='Zipcode'),
        ),
        migrations.AlterField(
            model_name='praticien',
            name='address',
            field=models.CharField(default='Address', max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='praticien',
            name='city',
            field=models.CharField(default='City', max_length=255, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='praticien',
            name='zipcode',
            field=models.CharField(default='00000', max_length=5, verbose_name='Zipcode'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='Last Name'),
        ),
    ]
