# from rest_framework.permissions import BasePermission

# from rest_framework import permissions

# class UserPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         if view.action == 'list':
#             return not request.user.is_guest
#         elif view.action == 'create':
#             return request.user.is_superuser
#         elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
#             return request.user.is_superuser
#         else:
#             return False
                                                                                                
#     def has_object_permission(self, request, view, obj):
#         # Deny actions on objects if the user is not authenticated
#         if not request.user.is_authenticated():
#             return False

#         if view.action == 'retrieve':
#             return obj ==  request.user.is_superuser
#         elif view.action in ['update', 'partial_update']:
#             return obj ==  request.user.is_superuser
#         elif view.action == 'destroy':
#             return request.user.is_superuser
#         else:
#             return False

from rest_framework import permissions

class IsStaffOwnerOrSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow superusers unrestricted access
        if request.user.is_superuser:
            return True
        if request.user.is_staff:
            return True
        if view.action =="post" and not request.user.is_superuser:
            return False
        # For non-superusers, only allow access to retrieve their own data
        if view.action == 'retrieve' and view.basename == 'staff':
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # Allow superusers unrestricted access
        if request.user.is_superuser:
            return True
        return False

        # For non-superusers, only allow access if they are the owner of the staff object
        # return obj.user == request.user
