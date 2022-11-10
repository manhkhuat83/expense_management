from django.urls import path
from statistic.views import StatisticView


urlpatterns = [
    path('statistic/', StatisticView.as_view()),
]