from django.conf import settings
from django.db import models


class AuditLog(models.Model):

    class ActionType(models.TextChoices):
        CREATE = "CREATE", "Create"
        UPDATE = "UPDATE", "Update"
        DELETE = "DELETE", "Delete"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    action = models.CharField(
        max_length=20,
        choices=ActionType.choices
    )

    model_name = models.CharField(max_length=100)

    object_id = models.PositiveIntegerField()

    description = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return (
            f"{self.user} - "
            f"{self.action} - "
            f"{self.model_name}"
        )