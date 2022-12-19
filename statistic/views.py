from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.db.models import Q
from expense.models import Expense, Income, IncomeCategory, ExpenseCategory
from datetime import datetime, timedelta


def validate_date(date_str):
    return bool(datetime.strptime(date_str, "%Y-%m-%d"))


def get_date_range(start, end):
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date()
    delta = end_date - start_date
    days = [start_date + timedelta(days=i) for i in range(delta.days + 1)]
    return list(map(lambda n: n.strftime("%Y-%m-%d"), days))


class StatisticIncomeExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, start_date=None, end_date=None):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        if not start_date or not end_date:
            err = {"err": "start_date and end_date are required"}
            return JsonResponse(err, status=400)
        if not validate_date(start_date) or not validate_date(end_date):
            err = {"err": "start_date and end_date must be in format YYYY-MM-DD"}
            return JsonResponse(err, status=400)
        days = get_date_range(start_date, end_date)
        count_responses = [None] * len(days)
        for day in days:
            expenses = Expense.objects.filter(
                Q(user_id=self.request.user) & Q(date=day)
            )
            incomes = Income.objects.filter(Q(user_id=self.request.user) & Q(date=day))
            count_responses[days.index(day)] = {
                "date": day,
                "total_incomes": sum([income.amount for income in incomes]),
                "total_expenses": sum([expense.amount for expense in expenses]),
            }
        data = {
            "data": count_responses,
        }
        return JsonResponse(data, status=200)


class StatisticIncomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, start_date=None, end_date=None):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        if not start_date or not end_date:
            err = {"err": "start_date and end_date are required"}
            return JsonResponse(err, status=400)
        if not validate_date(start_date) or not validate_date(end_date):
            err = {"err": "start_date and end_date must be in format YYYY-MM-DD"}
            return JsonResponse(err, status=400)
        categories = IncomeCategory.objects.filter(user_id=self.request.user)
        all_incomes = Income.objects.filter(
            Q(user_id=self.request.user) & Q(date__range=[start_date, end_date])
        )
        total_incomes = sum([income.amount for income in all_incomes])
        data = {}
        for category in categories:
            incomes = Income.objects.filter(
                Q(user_id=self.request.user)
                & Q(income_category_id=category)
                & Q(date__range=[start_date, end_date])
            )
            data.update({category.name: sum([income.amount for income in incomes])})
        data.update({"total_incomes": total_incomes})
        return JsonResponse(data, status=200)


class StatisticExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, start_date=None, end_date=None):
        start_date = request.GET.get("start_date")
        end_date = request.GET.get("end_date")
        if not start_date or not end_date:
            err = {"err": "start_date and end_date are required"}
            return JsonResponse(err, status=400)
        if not validate_date(start_date) or not validate_date(end_date):
            err = {"err": "start_date and end_date must be in format YYYY-MM-DD"}
            return JsonResponse(err, status=400)
        categories = ExpenseCategory.objects.filter(user_id=self.request.user)
        all_expenses = Expense.objects.filter(
            Q(user_id=self.request.user) & Q(date__range=[start_date, end_date])
        )
        total_expenses = sum([expense.amount for expense in all_expenses])
        data = {}
        for category in categories:
            expenses = Expense.objects.filter(
                Q(user_id=self.request.user)
                & Q(expense_category_id=category)
                & Q(date__range=[start_date, end_date])
            )
            data.update({category.name: sum([expense.amount for expense in expenses])})
        data.update({"total_expenses": total_expenses})
        return JsonResponse(data, status=200)
