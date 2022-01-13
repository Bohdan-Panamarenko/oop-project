from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView
from .models import Requisite, RequisiteHistory, RequisitePosterRole
from .forms import RequisiteForm, RequisiteHisForm, RequisiteRoleForm, RequisiteTypeForm
from .filters import RequisiteTypeFilter, RequisiteFilter


def main(request):
    if request.session['position'] != 2 and request.session['position'] != 4:
        return redirect('authorization')
    return render(request, "requisite/main.html", {'data': request.session['position']})


def requisite(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    output = Requisite.objects.all()
    typeFilter = RequisiteTypeFilter(request.GET, queryset=output)
    output = typeFilter.qs
    return render(request, 'requisite/requisite.html', {'requisite': output, 'typeFilter': typeFilter, 'data': request.session['position']})


def filter_requisite(request, pk):
    requisite = Requisite.objects.all()
    if pk == 1:
        requisite = requisite.order_by('id')
    elif pk == 2:
        requisite = requisite.order_by('name')
    elif pk == 3:
        requisite = requisite.order_by('requisite_type_id__type')

    typeFilter = RequisiteTypeFilter(request.GET, queryset=requisite)
    output = typeFilter.qs
    return render(request, 'requisite/requisite.html', {'requisite': output, 'typeFilter': typeFilter, 'data': request.session['position']})


def filter_req_his(request, pk):
    requisite = RequisiteHistory.objects.all()
    if pk == 1:
        requisite = requisite.order_by('requisite_id__name')
    elif pk == 2:
        requisite = requisite.order_by('price')
    elif pk == 3:
        requisite = requisite.order_by('description')

    requisiteFilter = RequisiteFilter(request.GET, queryset=requisite)
    output = requisiteFilter.qs
    return render(request, 'requisite/requisite_history.html', {'requisite': output,
                                                                'requisiteFilter': requisiteFilter,
                                                                'data': request.session['position']})


def filter_req_pos_role(request, pk):
    requisite = RequisitePosterRole.objects.all()
    if pk == 1:
        requisite = requisite.order_by('requisite_id__name')
    elif pk == 2:
        requisite = requisite.order_by('requisite_id_id')
    elif pk == 3:
        requisite = requisite.order_by('role_id__role_id__name')
    elif pk == 4:
        requisite = requisite.order_by('role_id_id')
    elif pk == 5:
        requisite = requisite.order_by('poster_id__performance_id__name')
    elif pk == 6:
        requisite = requisite.order_by('poster_id__performance_id_id')
    elif pk == 7:
        requisite = requisite.order_by('poster_id__date')

    requisiteFilter = RequisiteFilter(request.GET, queryset=requisite)
    output = requisiteFilter.qs
    return render(request, 'requisite/requisite_poster_role.html', {'requisite': output,
                                                                    'requisiteFilter': requisiteFilter,
                                                                    'data': request.session['position']})

def requisite_history(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    output = RequisiteHistory.objects.all()
    requisiteFilter = RequisiteFilter(request.GET, queryset=output)
    output = requisiteFilter.qs
    return render(request, 'requisite/requisite_history.html', {'requisite': output,
                                                                'requisiteFilter': requisiteFilter,
                                                                'data': request.session['position']})


def requisite_poster_role(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    output = RequisitePosterRole.objects.all()
    requisiteFilter = RequisiteFilter(request.GET, queryset=output)
    output = requisiteFilter.qs
    return render(request, 'requisite/requisite_poster_role.html', {'requisite': output,
                                                                    'requisiteFilter': requisiteFilter,
                                                                    'data': request.session['position']})


def create_requisite_type(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    form = RequisiteTypeForm()
    error = ''
    if request.method == "POST":
        form = RequisiteTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_requisite')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'requisite/create_requisite_type.html', data)


def create_requisite(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    form = RequisiteForm()
    error = ''
    if request.method == "POST":
        form = RequisiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('requisite')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'requisite/create_requisite.html', data)


def create_requisite_his(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    form = RequisiteHisForm()
    error = ''
    if request.method == "POST":
        form = RequisiteHisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('requisite_history')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'requisite/create_requisite_his.html', data)


def create_requisite_role(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    form = RequisiteRoleForm()
    error = ''
    if request.method == "POST":
        form = RequisiteRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('requisite_poster_role')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'requisite/create_requisite_role.html', data)


class RequisiteDeleteView(DeleteView):
    model = Requisite
    template_name = 'requisite/requisite_delete.html'
    success_url = '/requisite/'


class RequisiteHisDeleteView(DeleteView):
    model = RequisiteHistory
    template_name = 'requisite/requisite_delete.html'
    success_url = '/requisite/requisite_history/'


class RequisiteRoleDeleteView(DeleteView):
    model = RequisitePosterRole
    template_name = 'requisite/requisite_delete.html'
    success_url = '/requisite/requisite_poster_role/'


class RequisiteUpdateView(UpdateView):
    model = Requisite
    template_name = 'requisite/requisite_update.html'
    form_class = RequisiteForm


class RequisiteRoleUpdateView(UpdateView):
    model = RequisitePosterRole
    template_name = 'requisite/requisite_update.html'
    form_class = RequisiteRoleForm

