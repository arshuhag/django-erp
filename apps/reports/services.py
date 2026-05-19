from django.db.models import Count, Sum

from apps.employees.models import Employee
from apps.inventory.models import Product
from apps.sales.models import Order


class DashboardService:

    @staticmethod
    def get_dashboard_statistics():

        total_employees = Employee.objects.count()

        total_products = Product.objects.count()

        total_orders = Order.objects.count()

        total_revenue = (
            Order.objects.filter(
                payment_status='PAID'
            ).aggregate(
                total=Sum('total_amount')
            )['total'] or 0
        )

        low_stock_products = Product.objects.filter(
            stock_quantity__lte=5
        ).count()

        recent_orders = (
            Order.objects.select_related(
                'customer'
            ).order_by('-id')[:5]
        )

        return {
            'total_employees': total_employees,
            'total_products': total_products,
            'total_orders': total_orders,
            'total_revenue': total_revenue,
            'low_stock_products': low_stock_products,
            'recent_orders': recent_orders,
        }