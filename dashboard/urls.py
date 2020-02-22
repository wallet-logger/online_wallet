from django.urls import path

from . import views

urlpatterns = [
    path('home', views.dashboard_table, name='dashboard_table'),
]