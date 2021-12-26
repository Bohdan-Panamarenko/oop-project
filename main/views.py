from django.shortcuts import render
from employees.models import Account
from .forms import EmployeeForm


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
                return render(request, 'admin_main.html')
    form = EmployeeForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'authorization.html', data)