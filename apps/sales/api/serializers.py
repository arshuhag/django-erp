from rest_framework import serializers

from apps.sales.models import (
    Customer,
    Order,
    OrderItem,
)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemCreateSerializer(serializers.Serializer):

    product = serializers.IntegerField()

    quantity = serializers.IntegerField()


class OrderCreateSerializer(serializers.Serializer):

    customer = serializers.IntegerField()

    items = OrderItemCreateSerializer(
        many=True
    )