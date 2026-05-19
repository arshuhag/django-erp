from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.audits.models import AuditLog
from apps.audits.services import AuditService

from apps.inventory.models import Product
from apps.sales.models import (
    Order,
    OrderItem,
)


class OrderService:

    @staticmethod
    @transaction.atomic
    def create_order(
    *,
    user,
    customer_id,
    items
):

        order = Order.objects.create(
            customer_id=customer_id
        )

        for item in items:

            product = Product.objects.select_for_update().get(
                id=item['product']
            )

            quantity = item['quantity']

            if product.stock_quantity < quantity:

                raise ValidationError(
                    f"Insufficient stock for {product.name}"
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=product.price,
                subtotal=product.price * quantity
            )

            product.stock_quantity -= quantity

            product.save()

        order.update_total_amount()
        
        AuditService.log_action(
            user=user,
            action=AuditLog.ActionType.CREATE,
            model_name='Order',
            object_id=order.id,
            description=(
                f"Created order #{order.id}"
            )
        )

        return order