from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.api.permissions import IsAdmin
from apps.sales.models import Order
from apps.sales.services import OrderService

from .serializers import (
    OrderCreateSerializer,
    OrderSerializer,
)


class OrderListAPIView(ListAPIView):

    queryset = Order.objects.prefetch_related(
        'items'
    ).all()

    serializer_class = OrderSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]


class OrderCreateAPIView(CreateAPIView):

    serializer_class = OrderCreateSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin
    ]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        order = OrderService.create_order(
            user=request.user,
            customer_id=serializer.validated_data['customer'],
            items=serializer.validated_data['items']
        )

        response_serializer = OrderSerializer(order)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )