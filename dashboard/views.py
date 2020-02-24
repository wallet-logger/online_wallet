from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json

import mongoengine
from dashboard.models import DashboardTableEntry, PaymentDocument

def dashboard_table(request):
    data = [DashboardTableEntry.create_entry("june", "new york", 22, "2012/02/22", "clerk", "200")]
    return HttpResponse(serializers.serialize("json", data))

@api_view(['POST'])
@csrf_exempt
def create_payment_entry(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    page = PaymentDocument(payment_id=body["payment_id"] , user_id=body["user_id"], account=body["account"], category=body["category"], subcategory=body["subcategory"], contents=body["contents"], amount=body["amount"], currency_code=body["currency_code"], is_expense=body["is_expense"])
    page.tags = ['mongodb', 'mongoengine']
    page.save()
    return HttpResponse("SUCCESSFULLY ADDED")
