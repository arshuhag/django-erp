from rest_framework.permissions import BasePermission

from apps.accounts.models import User


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.Role.ADMIN


class IsHR(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.Role.HR


class IsAccountant(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.Role.ACCOUNTANT


class IsInventoryManager(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.Role.INVENTORY


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.Role.EMPLOYEE