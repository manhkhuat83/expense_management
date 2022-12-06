from django.urls import path
from expense.views import (
    IncomeView,
    IncomeByIdView,
    ExpenseView,
    ExpenseByIdView,
    CategoryView,
    CategoryWithIdView,
    IncomeExpenseByDateView,
    IncomeExpenseByCategoryIdView,
)


urlpatterns = [
    path("incomes", IncomeView.as_view()),
    path("incomes/<uuid:income_id>", IncomeByIdView.as_view()),
    path("expenses", ExpenseView.as_view()),
    path("expenses/<uuid:expense_id>", ExpenseByIdView.as_view()),
    path("categories", CategoryView.as_view()),
    path("categories/<uuid:category_id>", CategoryWithIdView.as_view()),
    path("incomes-expenses", IncomeExpenseByDateView.as_view()),
    path(
        "incomes-expenses/category/<uuid:category_id>",
        IncomeExpenseByCategoryIdView.as_view(),
    ),
]
