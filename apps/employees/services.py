from apps.employees.models import Employee


class EmployeeService:

    @staticmethod
    def get_all_employees():
        return Employee.objects.select_related(
            'user',
            'department',
            'designation'
        )