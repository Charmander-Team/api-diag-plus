from django.db import models

# Create your models here.
""" 
    To import that model for a migration, we need to tell Django 
    to include the app in the file diagPlus/settings.py at INSTALLED_APPS. 
    Check the variable on how it is imported.    
"""


class User(models.Model):
    username = models.CharField(max_length=110)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def __str__(self):
        return self.username
