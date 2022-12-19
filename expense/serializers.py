from expense.models import Income, Expense, IncomeCategory, ExpenseCategory
from rest_framework import serializers


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ("id", "user_id", "name")
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "name": {"required": True},
        }


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = (
            "id",
            "user_id",
            "income_category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "income_category_id": {"required": True},
            "description": {"required": True},
            "amount": {"required": True},
            "date": {"required": True},
        }


class UpdateIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = (
            "id",
            "user_id",
            "income_category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "income_category_id": {"required": False},
            "description": {"required": False},
            "amount": {"required": False},
            "date": {"required": False},
        }


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ("id", "user_id", "name")
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "name": {"required": True},
        }


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            "id",
            "user_id",
            "expense_category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "expense_category_id": {"required": True},
            "description": {"required": True},
            "amount": {"required": True},
            "date": {"required": True},
        }


class UpdateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            "id",
            "user_id",
            "expense_category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "expense_category_id": {"required": False},
            "description": {"required": False},
            "amount": {"required": False},
            "date": {"required": False},
        }
