from django.contrib import admin
from .models import employeeModel, FertilizerStockDetail, TestingReports, WorkUpdate

# Register your models here.


class employeeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'loginId')


class FertilizerStockDetailAdmin(admin.ModelAdmin):
    list_display = (
        'products',
        'date',
        'stock'
    )


class TestingReportsAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'seed_test',
        'soil_test',
        'other_reports',
    )


class WorkUpdateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'department',
        'work',
        'description',
    )


admin.site.register(employeeModel, employeeModelAdmin)
admin.site.register(FertilizerStockDetail, FertilizerStockDetailAdmin)
admin.site.register(TestingReports, TestingReportsAdmin)
admin.site.register(WorkUpdate, WorkUpdateAdmin)
