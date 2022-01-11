from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView

from .models import Employee, Hiring, Role, Account, Position, Roles
from .forms import EmployeeForm, PositionForm, RoleForm, HiringForm, RoleListForm


def main(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    return render(request, "employees/main.html")


def sort_roles_id_asc(request):
    output = Role.objects.all()
    output = output.order_by('id')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_id_desc(request):
    output = Role.objects.all()
    output = output.order_by('-id')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_name_asc(request):
    output = Role.objects.all()
    output = output.order_by('employee_id__last_name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_name_desc(request):
    output = Role.objects.all()
    output = output.order_by('-employee_id__last_name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_surname_asc(request):
    output = Role.objects.all()
    output = output.order_by('employee_id__first_name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_surname_desc(request):
    output = Role.objects.all()
    output = output.order_by('-employee_id__first_name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_role_asc(request):
    output = Role.objects.all()
    output = output.order_by('role_id__name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_role_desc(request):
    output = Role.objects.all()
    output = output.order_by('-role_id__name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_performance_asc(request):
    output = Role.objects.all()
    output = output.order_by('poster_id__performance_id__name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_performance_desc(request):
    output = Role.objects.all()
    output = output.order_by('-poster_id__performance_id__name')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_fee_asc(request):
    output = Role.objects.all()
    output = output.order_by('fee')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_roles_fee_desc(request):
    output = Role.objects.all()
    output = output.order_by('-fee')
    return render(request, 'employees/roles.html', {'roles': output})


def sort_hiring_id_asc(request):
    output = Hiring.objects.all()
    output = output.order_by('id')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_id_desc(request):
    output = Hiring.objects.all()
    output = output.order_by('-id')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_name_asc(request):
    output = Hiring.objects.all()
    output = output.order_by('employee_id__last_name')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_name_desc(request):
    output = Hiring.objects.all()
    output = output.order_by('-employee_id__last_name')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_surname_asc(request):
    output = Hiring.objects.all()
    output = output.order_by('employee_id__first_name')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_surname_desc(request):
    output = Hiring.objects.all()
    output = output.order_by('-employee_id__first_name')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_position_asc(request):
    output = Hiring.objects.all()
    output = output.order_by('position_id__position')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_position_desc(request):
    output = Hiring.objects.all()
    output = output.order_by('-position_id__position')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_date_asc(request):
    output = Hiring.objects.all()
    output = output.order_by('hiring_date')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_hiring_date_desc(request):
    output = Hiring.objects.all()
    output = output.order_by('-hiring_date')
    return render(request, 'employees/hiring.html', {'hiring': output})


def sort_roles_list_id_asc(request):
    output = Roles.objects.all()
    output = output.order_by('id')
    return render(request, 'employees/roles_list.html', {'roles': output})


def sort_roles_list_id_desc(request):
    output = Roles.objects.all()
    output = output.order_by('-id')
    return render(request, 'employees/roles_list.html', {'roles': output})


def sort_roles_list_name_asc(request):
    output = Roles.objects.all()
    output = output.order_by('name')
    return render(request, 'employees/roles_list.html', {'roles': output})


def sort_roles_list_name_desc(request):
    output = Roles.objects.all()
    output = output.order_by('-name')
    return render(request, 'employees/roles_list.html', {'roles': output})


def sort_roles_list_performance_asc(request):
    output = Roles.objects.all()
    output = output.order_by('performance_id__name')
    return render(request, 'employees/roles_list.html', {'roles': output})


def sort_roles_list_performance_desc(request):
    output = Roles.objects.all()
    output = output.order_by('-performance_id__name')
    return render(request, 'employees/roles_list.html', {'roles': output})


def sort_employees_id_asc(request):
    output = Employee.objects.all()
    output = output.order_by('id')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_id_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-id')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_phone_asc(request):
    output = Employee.objects.all()
    output = output.order_by('phone')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_phone_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-phone')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_address_asc(request):
    output = Employee.objects.all()
    output = output.order_by('address')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_address_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-address')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_positions_id_asc(request):
    output = Position.objects.all()
    output = output.order_by('id')
    return render(request, 'employees/positions.html', {'positions': output})


def sort_positions_id_desc(request):
    output = Position.objects.all()
    output = output.order_by('-id')
    return render(request, 'employees/positions.html', {'positions': output})


def sort_positions_name_asc(request):
    output = Position.objects.all()
    output = output.order_by('position')
    return render(request, 'employees/positions.html', {'positions': output})


def sort_positions_name_desc(request):
    output = Position.objects.all()
    output = output.order_by('-position')
    return render(request, 'employees/positions.html', {'positions': output})


def sort_employees_name_asc(request):
    output = Employee.objects.all()
    output = output.order_by('last_name')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_name_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-last_name')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_surname_asc(request):
    output = Employee.objects.all()
    output = output.order_by('first_name')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_surname_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-first_name')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_patronymic_asc(request):
    output = Employee.objects.all()
    output = output.order_by('patronymic')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_patronymic_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-patronymic')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_id_asc(request):
    output = Employee.objects.all()
    output = output.order_by('id')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_id_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-id')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_date_asc(request):
    output = Employee.objects.all()
    output = output.order_by('date_of_birth')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_date_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-date_of_birth')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_email_asc(request):
    output = Employee.objects.all()
    output = output.order_by('email')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_email_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-email')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_workbook_asc(request):
    output = Employee.objects.all()
    output = output.order_by('work_book')
    return render(request, 'employees/employees.html', {'employees': output})


def sort_employees_workbook_desc(request):
    output = Employee.objects.all()
    output = output.order_by('-work_book')
    return render(request, 'employees/employees.html', {'employees': output})


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


def employee_info(request):
    employees = Employee.objects.all()
    if request.GET:
        i = 0
        for employee in employees:
            i += 1
            if str(employee.id) == request.GET['id']:
                l = employee
    if request.POST:
        if request.POST['save']:
            employees[i].last_name = request.POST['name']
        elif request.POST['exit']:
            return render(request, 'employees/employees.html', {'employees': employees})
        elif request.POST['dismiss']:
            s = Employee.objects
    return render(request, "employees/employee_info.html", {'l': l})


def employees(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    output = Employee.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        surname = request.POST['surname']
        patronymic = request.POST['patronymic']
        work_book = request.POST['work_book']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        employees = []
        for l in output:
            if (str(l.id) == id or not id) and (l.last_name == name or not name) and (l.first_name == surname or not surname) and (l.patronymic == patronymic or not patronymic) and (l.work_book == work_book or not work_book) and (l.email == email or not email) and (str(l.phone) == phone or not phone) and (l.address == address or not address):
                employees.append(l)
        return render(request, 'employees/employees.html', {'employees': employees})
    return render(request, 'employees/employees.html', {'employees': output})


def hiring(request):
    if request.session['position'] != 2:
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
        return render(request, 'employees/hiring.html', {'hiring': hiring})
    return render(request, 'employees/hiring.html', {'hiring': output})


def roles(request):
    if request.session['position'] != 2:
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
        return render(request, 'employees/roles.html', {'roles': roles})
    return render(request, 'employees/roles.html', {'roles': output})


def positions(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    output = Position.objects.all()
    if request.method == "POST":
        id = request.POST['id']
        position = request.POST['position']
        positions = []
        for l in output:
            if (str(l.id) == id or not id) and (l.position == position or not position):
                positions.append(l)
        return render(request, 'employees/positions.html', {'positions': positions})
    return render(request, 'employees/positions.html', {'positions': output})


def roles_list(request):
    if request.session['position'] != 2:
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
        return render(request, 'employees/roles_list.html', {'roles': roles})
    return render(request, 'employees/roles_list.html', {'roles': output})


def create_employee(request):
    if request.session['position'] != 2:
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
        'error': error
    }
    return render(request, 'employees/create_employee.html', data)


def create_position(request):
    if request.session['position'] != 2:
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
        'error': error
    }
    return render(request, 'employees/create_position.html', data)


def create_role(request):
    if request.session['position'] != 2:
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
        'error': error
    }
    return render(request, 'employees/create_role.html', data)


def create_role_list(request):
    if request.session['position'] != 2:
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
        'error': error
    }
    return render(request, 'employees/create_role_list.html', data)


def create_hiring(request):
    if request.session['position'] != 2:
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
        'error': error
    }
    return render(request, 'employees/create_hiring.html', data)


