from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('convert/', views.CurrencyView.as_view(), name='convert'),
]
