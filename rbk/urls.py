"""rbk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import os
from django.urls import path
from . import views
from employee import views as employee_views
from farmer import views as farmer_views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('subsidy_status/', views.subsidy_status, name='subsidy_status'),
    path('farmer_login/', views.farmer_login, name='farmer_login'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('farmer_register/', views.farmer_register, name='farmer_register'),

    # farmer urls
    path('farmerHome/', farmer_views.farmerHome, name='farmerHome'),
    path('product_tracking/', farmer_views.product_tracking,
         name='product_tracking'),
    path('available_product/', farmer_views.available_product,
         name='available_product'),
    path('crops_types/', farmer_views.crops_types, name='crops_types'),
  
  
    path('feedback/<int:product_id>', farmer_views.feedback, name='feedback'),

    # employee urls

    path('employee_work_update/', employee_views.employee_work_update, name='employee_work_update'),
    path('fertilizer_distribution/', employee_views.fertilizer_distribution, name='fertilizer_distribution'),
    path('update_fertilizer_stock_details/', employee_views.update_fertilizer_stock_details, name='update_fertilizer_stock_details'),
    path('testing_reports/', employee_views.testing_reports, name='testing_reports'),

  
]
