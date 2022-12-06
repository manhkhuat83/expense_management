from django.db import models
from authentication.models import User
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Income(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False
    )
    description = models.TextField(null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=False
    )
    description = models.TextField(null=False, blank=False)
    amount = models.FloatField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
