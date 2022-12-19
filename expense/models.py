from django.db import models
from encrypted_fields import fields
from authentication.models import User
import uuid


class IncomeCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = fields.EncryptedCharField(max_length=100)

    def __str__(self):
        return self.name


class Income(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    income_category_id = models.ForeignKey(
        IncomeCategory, on_delete=models.CASCADE, null=False, blank=False
    )
    description = fields.EncryptedCharField(null=False, blank=False, max_length=100)
    amount = fields.EncryptedIntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)


class ExpenseCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = fields.EncryptedCharField(max_length=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    expense_category_id = models.ForeignKey(
        ExpenseCategory, on_delete=models.CASCADE, null=False, blank=False
    )
    description = fields.EncryptedCharField(null=False, blank=False, max_length=100)
    amount = fields.EncryptedIntegerField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)
