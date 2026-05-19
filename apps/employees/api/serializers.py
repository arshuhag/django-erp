from rest_framework import serializers

from apps.accounts.models import User
from apps.employees.models import (
    Department,
    Designation,
    Employee,
)


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name']


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ['id', 'title']


class EmployeeSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    department = DepartmentSerializer(read_only=True)

    designation = DesignationSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate_salary(self, value):

        if value < 0:
            raise serializers.ValidationError(
                "Salary cannot be negative."
            )

        return value