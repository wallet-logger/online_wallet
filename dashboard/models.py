from django.db import models

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