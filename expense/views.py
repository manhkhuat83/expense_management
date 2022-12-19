from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q
from expense.serializers import (
    IncomeSerializer,
    ExpenseSerializer,
    UpdateIncomeSerializer,
    UpdateExpenseSerializer,
    IncomeCategorySerializer,
    ExpenseCategorySerializer,
)
from expense.models import Income, Expense, IncomeCategory, ExpenseCategory
from drf_yasg.utils import swagger_auto_schema


class IncomeCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get all income categories",
        responses={200: IncomeCategorySerializer(many=True)},
    )
    def get(self, request):
        categories = IncomeCategory.objects.filter(user_id=self.request.user.id)
        serializer = IncomeCategorySerializer(categories, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Create new income category",
        responses={
            200: IncomeCategorySerializer,
            400: "Invalid data",
            303: "See other",
        },
        request_body=IncomeCategorySerializer,
    )
    def post(self, request):
        try:
            category = IncomeCategory.objects.get(
                Q(name=request.data.get("name")) & Q(user_id=self.request.user.id)
            )
            err = {"err": "See other"}
            return JsonResponse(err, status=303)
        except:
            pass
        serializer = IncomeCategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            category.user_id = self.request.user
            category.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ExpenseCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get all expense categories",
        responses={200: ExpenseCategorySerializer(many=True)},
    )
    def get(self, request):
        categories = ExpenseCategory.objects.filter(user_id=self.request.user.id)
        serializer = ExpenseCategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Create new expense category",
        responses={
            200: ExpenseCategorySerializer,
            400: "Invalid data",
            303: "See other",
        },
        request_body=ExpenseCategorySerializer,
    )
    def post(self, request):
        try:
            category = ExpenseCategory.objects.get(
                Q(name=request.data.get("name")) & Q(user_id=self.request.user.id)
            )
            err = {"err": "See other"}
            return JsonResponse(err, status=303)
        except:
            pass
        serializer = ExpenseCategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            category.user_id = self.request.user
            category.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class IncomeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get all incomes",
        responses={200: IncomeSerializer(many=True)},
    )
    def get(self, request):
        incomes = Income.objects.filter(user_id=self.request.user.id)
        serializer = IncomeSerializer(incomes, many=True)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Create new income",
        responses={200: IncomeSerializer, 400: "Invalid data"},
        request_body=IncomeSerializer,
    )
    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            income = serializer.save()
            income.user_id = self.request.user
            income.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get all expenses",
        responses={200: ExpenseSerializer(many=True)},
    )
    def get(self, request):
        expenses = Expense.objects.filter(user_id=self.request.user.id)
        serializer = ExpenseSerializer(expenses, many=True)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Create new expense",
        responses={200: ExpenseSerializer, 400: "Invalid data"},
        request_body=ExpenseSerializer,
    )
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            expense = serializer.save()
            expense.user_id = self.request.user
            expense.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class IncomeCategoryByIdView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get income category by id",
        responses={
            200: IncomeCategorySerializer,
            404: "Not found",
            403: "Permission denied",
        },
    )
    def get(self, request, income_category_id):
        try:
            category = IncomeCategory.objects.get(id=str(income_category_id).strip())
        except IncomeCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        serializer = IncomeCategorySerializer(category, many=False)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Update income category by id",
        responses={
            200: IncomeCategorySerializer,
            400: "Invalid data",
            403: "Permission denied",
            404: "Not found",
        },
    )
    def put(self, request, income_category_id):
        try:
            category = IncomeCategory.objects.get(id=str(income_category_id).strip())
        except IncomeCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        serializer = IncomeCategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            category.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete income category by id",
        responses={204: "Deleted", 404: "Not found", 403: "Permission denied"},
    )
    def delete(self, request, income_category_id):
        try:
            category = IncomeCategory.objects.get(id=str(income_category_id).strip())
        except IncomeCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        category.delete()
        msg = {"msg": "Deleted"}
        return JsonResponse(msg, status=204)


class ExpenseCategoryByIdView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get expense category by id",
        responses={
            200: ExpenseCategorySerializer,
            404: "Not found",
            403: "Permission denied",
        },
    )
    def get(self, request, expense_category_id):
        try:
            category = ExpenseCategory.objects.get(id=str(expense_category_id).strip())
        except ExpenseCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        serializer = ExpenseCategorySerializer(category, many=False)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Update expense category by id",
        responses={
            200: ExpenseCategorySerializer,
            404: "Not found",
            403: "Permission denied",
            400: "Invalid data",
        },
    )
    def put(self, request, expense_category_id):
        try:
            category = ExpenseCategory.objects.get(id=str(expense_category_id).strip())
        except ExpenseCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        serializer = IncomeCategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            category.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete expense category by id",
        responses={204: "Deleted", 404: "Not found", 403: "Permission denied"},
    )
    def delete(self, request, expense_category_id):
        try:
            category = ExpenseCategory.objects.get(id=str(expense_category_id).strip())
        except ExpenseCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        category.delete()
        msg = {"msg": "Deleted"}
        return JsonResponse(msg, status=204)


class IncomeByIdView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get income by id",
        responses={200: IncomeSerializer, 404: "Not found", 403: "Permission denied"},
    )
    def get(self, request, income_id):
        try:
            income = Income.objects.get(id=str(income_id).strip())
        except Income.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if income.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        serializer = IncomeSerializer(income, many=False)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Update income by id",
        responses={
            200: IncomeSerializer,
            404: "Not found",
            403: "Permission denied",
            400: "Invalid data",
        },
        request_body=UpdateIncomeSerializer,
    )
    def put(self, request, income_id):
        try:
            income = Income.objects.get(id=str(income_id).strip())
        except Income.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if income.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        serializer = UpdateIncomeSerializer(instance=income, data=request.data)
        if serializer.is_valid():
            income = serializer.save()
            income.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete income by id",
        responses={204: "Deleted", 404: "Not found", 403: "Permission denied"},
    )
    def delete(self, request, income_id):
        try:
            income = Income.objects.get(id=str(income_id).strip())
        except Income.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if income.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        income.delete()
        msg = {"msg": "Deleted"}
        return JsonResponse(msg, status=204)


class ExpenseByIdView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get expense by id",
        responses={200: ExpenseSerializer, 404: "Not found", 403: "Permission denied"},
    )
    def get(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=str(expense_id).strip())
        except Expense.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if expense.user_id != self.request.user:
            msg = {"msg": "Permission denied"}
            return JsonResponse(msg, status=403)
        serializer = ExpenseSerializer(expense, many=False)
        return JsonResponse(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Update expense by id",
        responses={
            200: ExpenseSerializer,
            404: "Not found",
            403: "Permission denied",
            400: "Invalid data",
        },
        request_body=UpdateExpenseSerializer,
    )
    def put(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=str(expense_id).strip())
        except Expense.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if expense.user_id != self.request.user:
            msg = {"msg": "Permission denied"}
            return JsonResponse(msg, status=403)
        serializer = UpdateExpenseSerializer(instance=expense, data=request.data)
        if serializer.is_valid():
            expense = serializer.save()
            expense.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    @swagger_auto_schema(
        operation_description="Delete expense by id",
        responses={204: "Deleted", 404: "Not found", 403: "Permission denied"},
    )
    def delete(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=str(expense_id).strip())
        except Expense.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if expense.user_id != self.request.user:
            msg = {"msg": "Permission denied"}
            return JsonResponse(msg, status=403)
        expense.delete()
        msg = {"msg": "Deleted"}
        return JsonResponse(msg, status=204)


class IncomeExpenseByDateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get income and expense by date",
        responses={200: "Data", 400: "Date is required (YYYY-mm-dd)"},
    )
    def get(self, request, date=None):
        date = request.GET.get("date", None)
        if not date:
            err = {"err": "Date is required (YYYY-mm-dd)"}
            return JsonResponse(err, status=400)
        incomes = Income.objects.filter(Q(user_id=self.request.user.id) & Q(date=date))
        expenses = Expense.objects.filter(
            Q(user_id=self.request.user.id) & Q(date=date)
        )
        total_incomes = sum([income.amount for income in incomes])
        total_expense = sum([expense.amount for expense in expenses])
        data = {
            "incomes": IncomeSerializer(incomes, many=True).data,
            "expenses": ExpenseSerializer(expenses, many=True).data,
            "total_incomes": total_incomes,
            "total_expenses": total_expense,
            "date": date,
        }
        return JsonResponse(data, status=200)


class IncomeByIncomeCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get income by income category id",
        responses={
            200: IncomeSerializer(many=True),
            404: "Not found",
            403: "Permission denied",
        },
    )
    def get(self, request, income_category_id):
        try:
            category = IncomeCategory.objects.get(id=str(income_category_id).strip())
        except IncomeCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        incomes = Income.objects.filter(
            Q(user_id=self.request.user.id) & Q(income_category_id=income_category_id)
        )
        serializer = IncomeSerializer(incomes, many=True)
        return JsonResponse(serializer.data, status=200)


class ExpenseByExpenseCategoryView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get expense by expense category id",
        responses={
            200: ExpenseSerializer(many=True),
            404: "Not found",
            403: "Permission denied",
        },
    )
    def get(self, request, expense_category_id):
        try:
            category = ExpenseCategory.objects.get(id=str(expense_category_id).strip())
        except ExpenseCategory.DoesNotExist:
            err = {"err": "Not found"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Permission denied"}
            return JsonResponse(err, status=403)
        expenses = Expense.objects.filter(
            Q(user_id=self.request.user.id) & Q(expense_category_id=expense_category_id)
        )
        serializer = ExpenseSerializer(expenses, many=True)
        return JsonResponse(serializer.data, status=200)
