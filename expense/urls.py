from django.urls import path
from expense.views import (
    IncomeCategoryView,
    IncomeCategoryByIdView,
    ExpenseCategoryView,
    ExpenseCategoryByIdView,
    IncomeView,
    IncomeByIdView,
    ExpenseView,
    ExpenseByIdView,
    IncomeExpenseByDateView,
    IncomeByIncomeCategoryView,
    ExpenseByExpenseCategoryView,
)


urlpatterns = [
    path("income-categories", IncomeCategoryView.as_view()),
    path(
        "income-categories/<uuid:income_category_id>", IncomeCategoryByIdView.as_view()
    ),
    path(
        "income-categories/<uuid:income_category_id>/incomes",
        IncomeByIncomeCategoryView.as_view(),
    ),
    path("expense-categories", ExpenseCategoryView.as_view()),
    path(
        "expense-categories/<uuid:expense_category_id>",
        ExpenseCategoryByIdView.as_view(),
    ),
    path(
        "expense-categories/<uuid:expense_category_id>/expenses",
        ExpenseByExpenseCategoryView.as_view(),
    ),
    path("incomes", IncomeView.as_view()),
    path("incomes/<uuid:income_id>", IncomeByIdView.as_view()),
    path("expenses", ExpenseView.as_view()),
    path("expenses/<uuid:expense_id>", ExpenseByIdView.as_view()),
    path("income-expense", IncomeExpenseByDateView.as_view()),
]
