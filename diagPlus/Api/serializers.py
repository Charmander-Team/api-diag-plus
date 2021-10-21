from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'phone',
            'zip_code',
            'city',
            'is_staff',
            'is_active',
            'date_joined',
        )
        model = User