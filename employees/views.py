from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView

from .models import Employee, Hiring, Role, Account, Position, Roles
from .forms import EmployeeForm, PositionForm, RoleForm, HiringForm, RoleListForm


def main(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    return render(request, "employees/main.html", {'data': request.session['position']})


def filter_employees(request, pk):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Employee.objects.all()
    if pk == 1:
        output = output.order_by('id')
    elif pk == 2:
        output = output.order_by('first_name')
    elif pk == 3:
        output = output.order_by('last_name')
    elif pk == 4:
        output = output.order_by('patronymic')
    elif pk == 5:
        output = output.order_by('work_book')
    elif pk == 6:
        output = output.order_by('email')
    elif pk == 7:
        output = output.order_by('phone')
    elif pk == 8:
        output = output.order_by('address')
    elif pk == 9:
        output = output.order_by('date_of_birth')

    return render(request, 'employees/employees.html', {'employees': output, 'data': request.session['position']})


def filter_roles(request, pk):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')

    output = Role.objects.all()
    if pk == 1:
        output = output.order_by('id')
    elif pk == 2:
        output = output.order_by('employee_id__first_name')
    elif pk == 3:
        output = output.order_by('employee_id__last_name')
    elif pk == 4:
        output = output.order_by('role_id__name')
    elif pk == 5:
        output = output.order_by('poster_id__performance_id__name')
    elif pk == 6:
        output = output.order_by('fee')

    return render(request, 'employees/roles.html', {'roles': output, 'data': request.session['position']})


def filter_roles_list(request, pk):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Roles.objects.all()
    if pk == 1:
        output = output.order_by('id')
    elif pk == 2:
        output = output.order_by('name')
    elif pk == 5:
        output = output.order_by('performance_id__name')

    return render(request, 'employees/roles_list.html', {'roles': output, 'data': request.session['position']})


def filter_positions(request, pk):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Position.objects.all()
    if pk == 1:
        output = output.order_by('id')
    elif pk == 2:
        output = output.order_by('position')

    return render(request, 'employees/positions.html', {'positions': output, 'data': request.session['position']})


def filter_hiring(request, pk):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Hiring.objects.all()
    if pk == 1:
        output = output.order_by('id')
    elif pk == 2:
        output = output.order_by('employee_id__first_name')
    elif pk == 3:
        output = output.order_by('employee_id__last_name')
    elif pk == 4:
        output = output.order_by('position_id__position')
    elif pk == 5:
        output = output.order_by('hiring_date')

    return render(request, 'employees/hiring.html', {'hiring': output, 'data': request.session['position']})


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_info.html'
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees/employee_update.html'

    form_class = EmployeeForm


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_delete.html'
    success_url = '/employees/employees/'


class HiringDetailView(DetailView):
    model = Hiring
    template_name = 'employees/hiring_info.html'
    context_object_name = 'hiring'


class HiringUpdateView(UpdateView):
    model = Hiring
    template_name = 'employees/hiring_update.html'

    form_class = HiringForm


class HiringDeleteView(DeleteView):
    model = Hiring
    template_name = 'employees/employee_delete.html'
    success_url = '/employees/hiring/'


class RolesDetailView(DetailView):
    model = Role
    template_name = 'employees/roles_info.html'
    context_object_name = 'role'


class RolesUpdateView(UpdateView):
    model = Role
    template_name = 'employees/roles_update.html'

    form_class = RoleForm


class RolesDeleteView(DeleteView):
    model = Role
    template_name = 'employees/roles_delete.html'
    success_url = '/employees/roles/'


class RolesListDetailView(DetailView):
    model = Roles
    template_name = 'employees/roles_list_info.html'
    context_object_name = 'role'


class RolesListUpdateView(UpdateView):
    model = Roles
    template_name = 'employees/roles_list_update.html'

    form_class = RoleListForm


class RolesListDeleteView(DeleteView):
    model = Roles
    template_name = 'employees/roles_list_delete.html'
    success_url = '/employees/roles_list/'


class PositionsDetailView(DetailView):
    model = Position
    template_name = 'employees/positions_info.html'
    context_object_name = 'position'


class PositionsUpdateView(UpdateView):
    model = Position
    template_name = 'employees/positions_update.html'

    form_class = PositionForm


class PositionsDeleteView(DeleteView):
    model = Position
    template_name = 'employees/positions_delete.html'
    success_url = '/employees/positions/'


def employees(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Employee.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        surname = request.POST['surname']
        work_book = request.POST['work_book']
        employees = []
        for l in output:
            if (str(l.id) == id or not id) and (l.last_name == name or not name) and (l.first_name == surname or not surname) and (l.work_book == work_book or not work_book):
                employees.append(l)
        return render(request, 'employees/employees.html', {'employees': employees, 'data': request.session['position']})
    return render(request, 'employees/employees.html', {'employees': output, 'data': request.session['position']})


def hiring(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Hiring.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        surname = request.POST['surname']
        position = request.POST['position']
        hiring = []
        for l in output:
            if (str(l.employee_id_id) == id or not id) and (l.employee_id.last_name == name or not name) and (l.employee_id.first_name == surname or not surname) and (l.position_id.position == position or not position):
                hiring.append(l)
        return render(request, 'employees/hiring.html', {'hiring': hiring, 'data': request.session['position']})
    return render(request, 'employees/hiring.html', {'hiring': output, 'data': request.session['position']})


def roles(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Role.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        surname = request.POST['surname']
        role = request.POST['role']
        performance = request.POST['performance']
        fee = request.POST['fee']
        roles = []
        for l in output:
            if (str(l.id) == id or not id) and (l.employee_id.last_name == name or not name) and (l.employee_id.first_name == surname or not surname) and (l.role_id.name == role or not role) and (l.poster_id.performance_id.name == performance or not performance) and (l.fee == fee or not fee):
                roles.append(l)
        return render(request, 'employees/roles.html', {'roles': roles, 'data': request.session['position']})
    return render(request, 'employees/roles.html', {'roles': output, 'data': request.session['position']})


def positions(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Position.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        position = request.POST['position']
        positions = []
        for l in output:
            if (str(l.id) == id or not id) and (l.position == position or not position):
                positions.append(l)
        return render(request, 'employees/positions.html', {'positions': positions, 'data': request.session['position']})
    return render(request, 'employees/positions.html', {'positions': output, 'data': request.session['position']})


def roles_list(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    output = Roles.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        performance = request.POST['performance']
        roles = []
        for l in output:
            if (str(l.id) == id or not id) and (l.name == name or not name) and (l.performance_id.name == performance or not performance):
                roles.append(l)
        return render(request, 'employees/roles_list.html', {'roles': roles, 'data': request.session['position']})
    return render(request, 'employees/roles_list.html', {'roles': output, 'data': request.session['position']})


def create_employee(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    form = EmployeeForm()
    error = ''
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'employees/create_employee.html', data)


def create_position(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    form = PositionForm()
    error = ''
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('positions')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'employees/create_position.html', data)


def create_role(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    form = RoleForm()
    error = ''
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roles')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'employees/create_role.html', data)


def create_role_list(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    form = RoleListForm()
    error = ''
    if request.method == "POST":
        form = RoleListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roles_list')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'employees/create_role_list.html', data)


def create_hiring(request):
    if request.session['position'] != 2 and request.session['position'] != 5:
        return redirect('authorization')
    form = HiringForm()
    error = ''
    if request.method == "POST":
        form = HiringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hiring')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'employees/create_hiring.html', data)


