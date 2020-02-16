from django.urls import path
from .views import HomePageView, ChartData
from .views import RateAdd

app_name = 'charts'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/chart/data/', ChartData.as_view(), name='chart'),
    path('add_rate/', RateAdd.as_view(), name='add_rate')
]