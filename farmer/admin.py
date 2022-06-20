from django.contrib import admin
from .models import ProductStatus, FarmerRegistrationModel, PurchaseAgroProduct, FarmerFeedback


# Register your models here.

class ProductStatusAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'farmer_id']


class FarmerRegistrationModelForm(admin.ModelAdmin):
    list_display = ['name', 'login_id', 'password',
                    'mobile', 'email', 'locality', 'address', 'state']


class PurchaseAgroProductAdmin(admin.ModelAdmin):
    list_display = [
        'products',
        'phone',
        'address',
        'farmer_name',
        'status'
    ]


class FarmerFeedbackAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'feedBack'
    ]


admin.site.register(ProductStatus, ProductStatusAdmin)
admin.site.register(FarmerRegistrationModel, FarmerRegistrationModelForm)
admin.site.register(PurchaseAgroProduct, PurchaseAgroProductAdmin)
admin.site.register(FarmerFeedback, FarmerFeedbackAdmin)
