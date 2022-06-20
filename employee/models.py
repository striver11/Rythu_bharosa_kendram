from django.db import models
from datetime import date
# Create your models here.
today = date.today()


class employeeModel(models.Model):
    import random
    name = models.CharField(max_length=100)
    loginId = models.CharField(max_length=6, unique=True, default=random.randint(
        100000, 999999), editable=False)


class WorkUpdate(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=today)
    department = models.CharField(max_length=5, choices=[
        ('dep1', "dep1"),
        ('dep2', "dep2"),
        ('dep3', "dep3"),
        ('dep4', "dep4"),
        ('dep5', "dep5")
    ])

    work = models.CharField(max_length=5, choices=[
        ('work1', "work1"),
        ('work2', "work2"),
        ('work3', "work3"),
        ('work4', "work4"),
        ('work5', "work5")
    ])
    description = models.TextField(null=True)


class FertilizerStockDetail(models.Model):
    products = models.CharField(max_length=3, choices=[
        ('p1', "p1"),
        ('p2', "p2"),
        ('p3', "p3"),
        ('p4', "p4"),
        ('p5', "p5"),

    ])
    date = models.DateField(default=today)
    stock = models.IntegerField()

class TestingReports(models.Model):
    seed_test = models.CharField(max_length=255)
    soil_test = models.CharField(max_length=255)
    date = models.DateField(default=today)
    other_reports = models.TextField()
    
