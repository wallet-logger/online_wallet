from django.urls import path

from . import views

urlpatterns = [
    path('home', views.dashboard_table, name='dashboard_table'),
    path('payment/create', views.create_payment_entry, name='create_payment_entry'),
    path('payment/getAll', views.retrieve_dashboard_table, name='retrieve_dashboard_table'),
    path('payment/getUser', views.retrieve_user_dashboard_table, name='retrieve_user_dashboard_table')
]