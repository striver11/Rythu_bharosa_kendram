from django.shortcuts import render
from .forms import employeLogineForm, WorkUpdateForm, FertilizerStockDetailForm, TestingReportsForm
from .models import employeeModel, WorkUpdate
from farmer.models import PurchaseAgroProduct

# Create your views here.


def employee_work_update(request):
    form = WorkUpdateForm()
    if request.method == 'POST':
        date = request.POST.get('date')
        department = request.POST.get('department')
        work = request.POST.get('work')
        description = request.POST.get('description')
        name = request.session['name']
        saveWorkUpdate = WorkUpdate(
            name=name,
            date=date,
            department=department,
            work=work,
            description=description
        )
        saveWorkUpdate.save()
        return render(request, 'employee/employee_work_update.html', {'form': form, 'msg': 'Work Updated'})
    else:
        return render(request, 'employee/employee_work_update.html', {'form': form})


def fertilizer_distribution(request):
    products_distributions = PurchaseAgroProduct.objects.all().order_by('-created_at')
    return render(request, 'employee/fertilizer_distribution.html', {'products_distributions': products_distributions})


def update_fertilizer_stock_details(request):
    if request.method == 'POST':
        form = FertilizerStockDetailForm(request.POST)
        if form.is_valid():
            form.save()
            form = FertilizerStockDetailForm()
            return render(request, 'employee/update_fertilizer_stock_details.html', {'form': form, 'msg': 'Stock Updated'})

    else:

        form = FertilizerStockDetailForm()
        return render(request, 'employee/update_fertilizer_stock_details.html', {'form': form})


def testing_reports(request):
    if request.method == 'POST':
        form = TestingReportsForm(request.POST)
        if form.is_valid():
            form.save()
            form = TestingReportsForm()
            return render(request, 'employee/testing_reports.html', {'form': form, 'msg': 'Reports Updated'})
    else:
        form = TestingReportsForm()
        return render(request, 'employee/testing_reports.html', {'form': form})
