from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "ADMIN"


class IsHR(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "HR"


class IsAccountant(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == "ACCOUNTANT"