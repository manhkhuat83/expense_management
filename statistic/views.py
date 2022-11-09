from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.db.models import Q
from expense.models import Expense, Income, Category
from datetime import datetime


def validate_date(date_str):
    return bool(datetime.strptime(date_str, '%Y-%m-%d'))


class StatisticView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, start_date=None, end_date=None):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if not start_date or not end_date:
            err = {'err': 'start_date and end_date are required'}
            return JsonResponse(err, status=400)
        if not validate_date(start_date) or not validate_date(end_date):
            err = {'err': 'start_date and end_date must be in format YYYY-MM-DD'}
            return JsonResponse(err, status=400)


