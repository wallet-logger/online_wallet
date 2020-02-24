from django.urls import path

from . import views

urlpatterns = [
    path('home', views.dashboard_table, name='dashboard_table'),
    path('payment/create', views.create_payment_entry, name='create_payment_entry'),
]