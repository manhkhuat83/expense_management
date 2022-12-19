from django.urls import path, include
from django.conf import settings

api_decorate = lambda endpoint: settings.API_PREFIX + endpoint

urlpatterns = [
    path(api_decorate(""), include("authentication.urls")),
    path(api_decorate(""), include("expense.urls")),
    path(api_decorate(""), include("statistic.urls")),
]
