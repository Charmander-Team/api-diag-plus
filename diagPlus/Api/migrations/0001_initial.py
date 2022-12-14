# Generated by Django 4.0 on 2022-04-30 17:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Article')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.PositiveIntegerField(verbose_name='Type')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255, verbose_name='Reason')),
                ('pathology_bot', models.PositiveIntegerField()),
                ('pathology_practicien', models.PositiveIntegerField()),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pathology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Speciality')),
                ('detail', models.CharField(max_length=255, verbose_name='Detail')),
                ('practicien_speciality', models.CharField(max_length=255, verbose_name='Practicien Speciality')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('zipcode', models.CharField(max_length=5, verbose_name='Zipcode')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('weight', models.PositiveIntegerField(verbose_name='Weight')),
                ('height', models.PositiveIntegerField(verbose_name='Height')),
                ('origin', models.CharField(max_length=255, verbose_name='Origin')),
                ('smoker', models.BooleanField(verbose_name='Smoker')),
                ('is_drinker', models.BooleanField(verbose_name='Drinker')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('domain', models.PositiveIntegerField(verbose_name='Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Speciality')),
                ('definition', models.CharField(max_length=255, verbose_name='Defintion')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('permission', models.PositiveIntegerField(default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Speciality')),
                ('detail', models.CharField(max_length=255, verbose_name='Detail')),
                ('pathologies', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.pathology')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(verbose_name='Response')),
                ('diagnostic', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.diagnostic')),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.question')),
            ],
        ),
        migrations.CreateModel(
            name='ReportPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('contenu', models.CharField(max_length=255, verbose_name='Content')),
                ('attachment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.attachment')),
                ('patients', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Speciality')),
                ('detail', models.CharField(max_length=255, verbose_name='Detail')),
                ('pathologies', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.pathology')),
            ],
        ),
        migrations.CreateModel(
            name='Praticien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('zipcode', models.CharField(max_length=5, verbose_name='Zipcode')),
                ('speciality', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.speciality')),
                ('users', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.DateField()),
                ('start_hours', models.DateTimeField()),
                ('end_hours', models.DateTimeField()),
                ('practiciens', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.praticien')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.user'),
        ),
        migrations.AddField(
            model_name='pathology',
            name='speciality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.speciality'),
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antecedent', models.CharField(max_length=255, verbose_name='Antecedent')),
                ('allergy', models.CharField(max_length=255, verbose_name='Allergy')),
                ('important_act', models.CharField(max_length=255, verbose_name='Important Act')),
                ('organ_donation', models.CharField(max_length=255, verbose_name='Organ Donation')),
                ('previous_medication', models.CharField(max_length=255, verbose_name='Previous Medication')),
                ('current_medication', models.CharField(max_length=255, verbose_name='Current Medication')),
                ('patients', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.patient')),
            ],
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='patients',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.patient'),
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='practiciens',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.praticien'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.DateTimeField()),
                ('end_hour', models.DateTimeField()),
                ('date', models.DateTimeField()),
                ('reason', models.TextField(verbose_name='Reason')),
                ('physical', models.BooleanField(verbose_name='Physical')),
                ('patients', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.patient')),
                ('practiciens', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.praticien')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('users', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Api.user')),
            ],
        ),
    ]
