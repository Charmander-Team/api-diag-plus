from rest_framework.permissions import BasePermission
from rest_framework import permissions


class isAdminAuthenticated(BasePermission):
    # check if the user authenticated is an admin
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class isOwnerOrReadOnly(BasePermission):
    # check if the user is the owner of the object
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        return False
