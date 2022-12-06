from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from django.db.models import Q
from expense.serializers import (
    IncomeSerializer,
    ExpenseSerializer,
    UpdateIncomeSerializer,
    UpdateExpenseSerializer,
    CategorySerializer,
)
from expense.models import Income, Expense, Category


class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, page=None, size=None):
        page = request.GET.get("page", None)
        size = request.GET.get("size", None)
        categories = Category.objects.filter(user_id=self.request.user.id)
        if page and size:
            paginator = PageNumberPagination()
            paginator.page_size = size
            paginator.page = page
            categories = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(categories, many=True)
        data = {
            "data": serializer.data,
            "page": int(page if page else 1),
            "size": int(size if size else len(categories)),
        }
        return JsonResponse(data, status=200)

    def post(self, request):
        try:
            category = Category.objects.get(
                Q(name=request.data.get("name")) & Q(user_id=self.request.user.id)
            )
            err = {"err": "Category with name already exists"}
            return JsonResponse(err, status=303)
        except:
            pass
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            category.user_id = self.request.user
            category.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class IncomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, page=None, size=None):
        page = request.GET.get("page", None)
        size = request.GET.get("size", None)
        incomes = Income.objects.filter(user_id=self.request.user.id)
        if page and size:
            paginator = PageNumberPagination()
            paginator.page_size = size
            incomes = paginator.paginate_queryset(incomes, request)
        serializer = IncomeSerializer(incomes, many=True)
        data = {
            "data": serializer.data,
            "page": int(page if page else 1),
            "size": int(size if size else len(incomes)),
        }
        return JsonResponse(data, status=200)

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

    def get(self, request, page=None, size=None):
        page = request.GET.get("page", None)
        size = request.GET.get("size", None)
        expenses = Expense.objects.filter(user_id=self.request.user.id)
        if page and size:
            paginator = PageNumberPagination()
            paginator.page_size = size
            expenses = paginator.paginate_queryset(expenses, request)
        serializer = ExpenseSerializer(expenses, many=True)
        data = {
            "data": serializer.data,
            "page": int(page if page else 1),
            "size": int(size if size else len(expenses)),
        }
        return JsonResponse(data, status=200)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            expense = serializer.save()
            expense.user_id = self.request.user
            expense.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class CategoryWithIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=str(category_id).strip())
        except Category.DoesNotExist:
            err = {"err": "Category with id does not exist"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Don't have permission to access this category"}
            return JsonResponse(err, status=403)
        serializer = CategorySerializer(category, many=False)
        return JsonResponse(serializer.data, status=200)

    def put(self, request, category_id):
        try:
            category = Category.objects.get(id=str(category_id).strip())
        except Category.DoesNotExist:
            err = {"err": "Category with id does not exist"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Don't have permission to access this category"}
            return JsonResponse(err, status=403)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            category.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, category_id):
        try:
            category = Category.objects.get(id=str(category_id).strip())
        except Category.DoesNotExist:
            err = {"err": "Category with id does not exist"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Don't have permission to access this category"}
            return JsonResponse(err, status=403)
        category.delete()
        msg = {"msg": "Category deleted successfully"}
        return JsonResponse(msg, status=204)


class IncomeByIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, income_id):
        try:
            income = Income.objects.get(id=str(income_id).strip())
        except Income.DoesNotExist:
            err = {"err": "Income with id does not exist"}
            return JsonResponse(err, status=404)
        if income.user_id != self.request.user:
            err = {"err": "Don't have permission to access this income"}
            return JsonResponse(err, status=403)
        serializer = IncomeSerializer(income, many=False)
        return JsonResponse(serializer.data, status=200)

    def put(self, request, income_id):
        try:
            income = Income.objects.get(id=str(income_id).strip())
        except Income.DoesNotExist:
            err = {"err": "Income with id does not exist"}
            return JsonResponse(err, status=404)
        if income.user_id != self.request.user:
            err = {"err": "Don't have permission to access this income"}
            return JsonResponse(err, status=403)
        serializer = UpdateIncomeSerializer(instance=income, data=request.data)
        if serializer.is_valid():
            income = serializer.save()
            income.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, income_id):
        try:
            income = Income.objects.get(id=str(income_id).strip())
        except Income.DoesNotExist:
            err = {"err": "Income with id does not exist"}
            return JsonResponse(err, status=404)
        if income.user_id != self.request.user:
            err = {"err": "Don't have permission to access this income"}
            return JsonResponse(err, status=403)
        income.delete()
        msg = {"msg": "Income deleted successfully"}
        return JsonResponse(msg, status=204)


class ExpenseByIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=str(expense_id).strip())
        except Expense.DoesNotExist:
            err = {"err": "Expense with id does not exist"}
            return JsonResponse(err, status=404)
        if expense.user_id != self.request.user:
            msg = {"msg": "Don't have permission to access this expense"}
            return JsonResponse(msg, status=403)
        serializer = ExpenseSerializer(expense, many=False)
        return JsonResponse(serializer.data, status=200)

    def put(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=str(expense_id).strip())
        except Expense.DoesNotExist:
            err = {"err": "Expense with id does not exist"}
            return JsonResponse(err, status=404)
        if expense.user_id != self.request.user:
            msg = {"msg": "Don't have permission to access this expense"}
            return JsonResponse(msg, status=403)
        serializer = UpdateExpenseSerializer(instance=expense, data=request.data)
        if serializer.is_valid():
            expense = serializer.save()
            expense.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, expense_id):
        try:
            expense = Expense.objects.get(id=str(expense_id).strip())
        except Expense.DoesNotExist:
            err = {"err": "Expense with id does not exist"}
            return JsonResponse(err, status=404)
        if expense.user_id != self.request.user:
            msg = {"msg": "Don't have permission to access this expense"}
            return JsonResponse(msg, status=403)
        expense.delete()
        msg = {"msg": "Expense deleted successfully"}
        return JsonResponse(msg, status=204)


class IncomeExpenseByDateView(APIView):
    permission_classes = [IsAuthenticated]

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


class IncomeExpenseByCategoryIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=str(category_id).strip())
        except Category.DoesNotExist:
            err = {"err": "Category with id does not exist"}
            return JsonResponse(err, status=404)
        if category.user_id != self.request.user:
            err = {"err": "Don't have permission to access this category"}
            return JsonResponse(err, status=403)
        incomes = Income.objects.filter(
            Q(user_id=self.request.user.id) & Q(category_id=category_id)
        )
        expenses = Expense.objects.filter(
            Q(user_id=self.request.user.id) & Q(category_id=category_id)
        )
        data = {
            "category": CategorySerializer(category, many=False).data,
            "incomes": IncomeSerializer(incomes, many=True).data,
            "expenses": ExpenseSerializer(expenses, many=True).data,
        }
        return JsonResponse(data, status=200)
