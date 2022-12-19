from django.urls import path
from statistic.views import (
    StatisticIncomeExpenseView,
    StatisticIncomeView,
    StatisticExpenseView,
)


urlpatterns = [
    path("statistic/common", StatisticIncomeExpenseView.as_view()),
    path("statistic/income", StatisticIncomeView.as_view()),
    path("statistic/expense", StatisticExpenseView.as_view()),
]
