from django.shortcuts import render
<<<<<<< HEAD
from employees.models import Account, Employee, Position, Hiring
from .forms import EmployeeForm

from django.contrib.auth import authenticate, login, logout


def main(request):
    return render(request, 'main.html')


def authorization(request):
    error = ''
    if request.method == "POST":
        error = 'Wrong values!'
        form = EmployeeForm(request.POST)
        accounts = Account.objects.all()
        for el in accounts:
            if str(el.employee_id_id) == form['employee_id'].data and el.login == form['login'].data and el.password == form['password'].data:
                employees = Hiring.objects.all()
                positions = []
                for employee in employees:
                    if el.employee_id == employee.employee_id:
                        positions.append(employee.position_id)

                position = positions[-1].id
                response = render(request, 'roles_employee.html', {'employee': el.employee_id})
                request.session['position'] = position
                request.session['employee_id'] = el.employee_id_id
                if position == 2:
                    return render(request, 'admin_main.html', {'employee': el.employee_id})
                if position == 1:
                    return render(request, 'employee_main.html', {'employee': el.employee_id})
    form = EmployeeForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'authorization.html', data)
=======

# Create your views here.

def main(request):
    return render(request, 'main.html')
>>>>>>> 2e166d30e963d225d123d3ad03c11980f04e4c4d
