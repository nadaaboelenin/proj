from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employees')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list_employees.html', {'employees': employees})

def delete_by_age(request):
    if request.method == "POST":
        age = request.POST.get('age')
        Employee.objects.filter(age=age).delete()
        return redirect('list_employees')
    return render(request, 'employees/delete_by_age.html')

def update_salary(request):
    if request.method == "POST":
        name = request.POST.get('name')
        salary = request.POST.get('salary')
        Employee.objects.filter(name=name).update(salary=salary)
        return redirect('list_employees')
    return render(request, 'employees/update_salary.html')
