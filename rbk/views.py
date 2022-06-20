from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from farmer.forms import FarmerRegistrationForm
from farmer.models import FarmerRegistrationModel
from employee.models import employeeModel


def index(request):
    return render(request, 'index.html')


def farmer_register(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        # print('FORM::::', form)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = FarmerRegistrationForm()
            return render(request, 'farmer_registrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = FarmerRegistrationForm()
    return render(request, 'farmer_registrations.html', {'form': form})


def farmer_login(request):
    if request.method == 'POST':
        login_id = request.POST.get('login_id')
        password = request.POST.get('password')
        print('loginId:', login_id)
        print('password:', password)
        try:
            farmer = FarmerRegistrationModel.objects.get(
                login_id=login_id,
                password=password
            )

            if farmer:

                request.session['login_id'] = login_id
                request.session['name'] = farmer.name
                print('farmer:',  request.session.get('name'))
                return render(request, 'farmer/formerHome.html')
            else:
                messages.error(request, 'Invalid Login Id')
                return render(request, 'farmer_login.html')
        except Exception as e:
            print("=== 0 =====", e)
            messages.error(request, 'Invalid Login Id/Password')
            return render(request, 'farmer_login.html')

    else:
        return render(request, 'farmer_login.html')


def subsidy_status(request):
    return render(request, 'subsidy_status.html')


def employee_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        loginId = request.POST.get('loginId')
        print('loginId:', name)
        print('password:', loginId)
        try:
            employee = employeeModel.objects.get(
                name=name,
                loginId=loginId
            )

            if employee:

                request.session['name'] = name
                request.session['loginId'] = loginId
                print('employee:',  request.session.get('name'))
                return render(request, 'employee/employeeHome.html')
            else:
                messages.error(request, 'Invalid Name/LoginId')
                return render(request, 'employeeLogin.html')
        except Exception as e:
            print("=== 0 =====", e)
            messages.error(request, 'Invalid Name/LoginId')
            return render(request, 'employeeLogin.html')

    else:
        return render(request, 'employeeLogin.html')




