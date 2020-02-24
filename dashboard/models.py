from django.db import models
import mongoengine
import datetime

# Create your models here.
class DashboardTableEntry(models.Model):
    name = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    age = models.IntegerField()
    startDate = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)

    @classmethod
    def create_entry(cls, name, office, age, startDate, position, salary):
        return cls(name=name, office=office, age=age, startDate=startDate, position=position, salary=salary)


class PaymentDocument(mongoengine.Document):
    payment_id = mongoengine.IntField(primary_key=True, required=True)
    user_id = mongoengine.IntField(required=True)
    time_created = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    account = mongoengine.StringField(max_length=200, required=True)
    category = mongoengine.StringField(max_length=100, required=True)
    subcategory = mongoengine.StringField(max_length=100, default="", required=False)
    contents = mongoengine.StringField(max_length=200, default="", required=False)
    amount = mongoengine.FloatField(min_value=0, required=True)
    currency_code = mongoengine.StringField(max_length=10, required=True)
    is_expense = mongoengine.BooleanField(required=True)
    

class UserDocument(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True, required=True)
    username = mongoengine.StringField(unique=True, required=True)
    passwordHash = mongoengine.StringField(required=True)
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)

class SettingsDocument(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True, required=True)
    