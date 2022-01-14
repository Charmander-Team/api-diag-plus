""" Admin Panel"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    """Custom Form for user creation on the admin panel"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Speciality)
admin.site.register(Question)
admin.site.register(Patient)
admin.site.register(ReportPatient)
admin.site.register(Files)
admin.site.register(Appointment)
admin.site.register(Praticien)
admin.site.register(Admin)
admin.site.register(Planning)
admin.site.register(Diagnostic)
admin.site.register(Response)
admin.site.register(Reason)
admin.site.register(Symptom)
admin.site.register(Pathology)
