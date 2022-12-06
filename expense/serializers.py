from expense.models import Income, Expense, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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
            "category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "category_id": {"required": True},
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
            "category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "category_id": {"required": False},
            "description": {"required": False},
            "amount": {"required": False},
            "date": {"required": False},
        }


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            "id",
            "user_id",
            "category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "category_id": {"required": True},
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
            "category_id",
            "description",
            "amount",
            "date",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"read_only": True},
            "category_id": {"required": False},
            "description": {"required": False},
            "amount": {"required": False},
            "date": {"required": False},
        }
