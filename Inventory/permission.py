from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        # Allow superusers unrestricted access
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated and request.user.is_Manager:
            return True
        # if view.action =="post" and not request.user.is_superuser:
        #     return False
        # # For non-superusers, only allow access to retrieve their own data
        # if view.action == 'retrieve' and view.basename == 'staff':
        #     return True

        return False

    def has_object_permission(self, request, view, obj):
        # Allow superusers unrestricted access
        if request.user.is_authenticated and request.user.is_Manager:
            return True
        return False