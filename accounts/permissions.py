from rest_framework import permissions

class IsNotDeleted(permissions.BasePermission):
   
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and not request.user.is_deleted
