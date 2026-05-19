from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated

from apps.accounts.api.permissions import (
    IsAdmin,
    IsInventoryManager,
)
from apps.inventory.models import Product

from .serializers import ProductSerializer


class ProductListAPIView(ListAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsInventoryManager
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filterset_fields = [
        'category',
        'warehouse',
    ]

    search_fields = [
        'name',
        'sku',
    ]


class ProductCreateAPIView(CreateAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsInventoryManager
    ]