from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from apps.accounts.api.permissions import IsAdmin, IsHR
from apps.employees.models import Employee
from apps.employees.services import EmployeeService

from .serializers import (
    EmployeeCreateSerializer,
    EmployeeSerializer,
)


class EmployeeListAPIView(ListAPIView):

    serializer_class = EmployeeSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHR
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_fields = [
        'department',
        'designation',
    ]

    search_fields = [
        'employee_id',
        'user__username',
    ]

    def get_queryset(self):
        return EmployeeService.get_all_employees()


class EmployeeCreateAPIView(CreateAPIView):

    queryset = Employee.objects.all()

    serializer_class = EmployeeCreateSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHR
    ]


class EmployeeDetailAPIView(RetrieveAPIView):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHR
    ]


class EmployeeUpdateAPIView(UpdateAPIView):

    queryset = Employee.objects.all()

    serializer_class = EmployeeCreateSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHR
    ]


class EmployeeDeleteAPIView(DestroyAPIView):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHR
    ]