from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from django.utils.datetime_safe import strftime

from employees.models import Role, Employee
from requisite.models import RequisitePosterRole
from employees.forms import EmployeeForm


def admin(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    return render(request, 'admin_main.html')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'info_employee.html'
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'update_employee.html'

    form_class = EmployeeForm


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'delete_employee.html'
    success_url = ''


def requisite_employee(request, pk):
    if pk != request.session['employee_id']:
        return redirect('authorization')
    if not request.session['employee_id']:
        return render(request, 'authorization.html')
    requisite = RequisitePosterRole.objects.filter(role_id__employee_id=pk)
    data = {'requisite': requisite}
    return render(request, 'requisite_employee.html', data)


def roles_employee(request, pk):
    if pk != request.session['employee_id']:
        return redirect('authorization')
    if not request.session['employee_id']:
        return render(request, 'authorization.html')
    roles = Role.objects.filter(employee_id_id=pk)
    data = {'roles': roles}
    return render(request, 'roles_employee.html', data)


def salary(request, pk):
    result = Role.objects.filter(employee_id_id=pk).order_by('poster_id__date')
    roles = {}
    for i in range(len(result)):
        d = strftime(result[i].poster_id.date, "%m/%Y")
        if d in roles:
            roles[d] = roles[d] + result[i].fee
        else:
            roles[d] = result[i].fee

    data = {'roles': roles.items()}

    return render(request, 'salary.html', data)


def employee_main(request):
    position = request.session['employee_id']
    return render(request, 'employee_main.html', {'employee': position})
