from rest_framework import serializers

from apps.sales.models import Order


class RecentOrderSerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source='customer.name'
    )

    class Meta:
        model = Order
        fields = [
            'id',
            'customer_name',
            'total_amount',
            'payment_status',
            'order_date',
        ]