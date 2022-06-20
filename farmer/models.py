from django.db import models
import random

# Create your models here.


class FarmerRegistrationModel(models.Model):
    # Create your models here.

    name = models.CharField(max_length=100)
    login_id = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=100)
    locality = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.login_id

    class Meta:
        db_table = 'FarmerRegistration'


class ProductStatus(models.Model):
    title = models.CharField(max_length=10, default=random.randint(
        1000000000, 9999999999), unique=True)
    status = models.BooleanField(default=False)
    farmer_id = models.ForeignKey(
        FarmerRegistrationModel, on_delete=models.CASCADE)


class PurchaseAgroProduct(models.Model):

    products = models.CharField(max_length=3, choices=[
        ('p1', "p1"),
        ('p2', "p2"),
        ('p3', "p3"),
        ('p4', "p4"),
        ('p5', "p5"),

    ])
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    farmer_name = models.CharField(max_length=255)
    status = models.BooleanField()

    def __str__(self):
        return str(self.products)


class FarmerFeedback(models.Model):
    product = models.CharField(max_length=20)
    feedBack = models.TextField()
