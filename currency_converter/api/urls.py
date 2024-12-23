from django.urls import path

from api import views

urlpatterns = [
    path('', views.CurrencyView.as_view()),
]
