<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.db.models.functions import TruncMonth, ExtractMonth
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, DateField

from employees.models import Role
from requisite.models import RequisitePosterRole


def admin(request):
    if request.session['position_id'] != 2:
        return redirect('authorization')
    return render(request, 'admin_main.html')


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
    #roles = Role.objects.filter(employee_id_id=pk)

    #result = Role.objects.values_list('poster_id__date__month', 'poster_id_date__year').annotate(totale=Sum('fee')).values_list('poster_id_date__year')

    #result = Role.objects.annotate(date=TruncMonth('poster_id__date')).values('date').annotate(salary=Sum('fee'))
    result = Role.objects.filter(employee_id_id=pk).values('poster_id__date').annotate(salary=Sum('fee'))
    #result = (roles.values_list('poster_id__date', 'fee').annotate(salary=Sum('fee')).order_by('poster_id__date'))
    #roles = (roles.order_by('poster_id__date').values('poster_id__date__month').aggregate(salary=Sum('fee')))
    data = {'roles': result}

    return render(request, 'salary.html', data)


def employee_main(request):
    return render(request, 'employee_main.html')
=======
from django.shortcuts import render

# Create your views here.

def admin(request):
    return render(request, 'admin_main.html')
>>>>>>> 2e166d30e963d225d123d3ad03c11980f04e4c4d
