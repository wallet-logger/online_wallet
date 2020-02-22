from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from dashboard.models import DashboardTableEntry

# Create your views here.

def dashboard_table(request):
    data = [DashboardTableEntry.create_entry("june", "new york", 22, "2012/02/22", "clerk", "200")]
    return HttpResponse(serializers.serialize("json", data))
