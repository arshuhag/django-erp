from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.api.permissions import IsAdmin
from apps.reports.services import DashboardService

from .serializers import RecentOrderSerializer


class DashboardAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def get(self, request):

        data = DashboardService.get_dashboard_statistics()

        recent_orders = RecentOrderSerializer(
            data['recent_orders'],
            many=True
        ).data

        return Response({
            'total_employees':
                data['total_employees'],

            'total_products':
                data['total_products'],

            'total_orders':
                data['total_orders'],

            'total_revenue':
                data['total_revenue'],

            'low_stock_products':
                data['low_stock_products'],

            'recent_orders':
                recent_orders,
        })