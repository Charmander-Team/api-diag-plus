# Generated by Django 4.0 on 2022-02-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_rename_attachments_attachment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Article')),
                ('image', models.ImageField(upload_to='images')),
                ('description', models.TextField(verbose_name='Description')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='permission',
            field=models.PositiveIntegerField(default=1),
        ),
    ]