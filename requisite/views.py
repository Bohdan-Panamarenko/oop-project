from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, DeleteView
from .models import Requisite, RequisiteHistory, RequisitePosterRole
from .forms import RequisiteForm, RequisiteHisForm, RequisiteRoleForm, RequisiteTypeForm
from .filters import RequisiteTypeFilter, RequisiteFilter


def main(request):
    if request.session['position_id'] != 2:
        return redirect('authorization')
    return render(request, "Requisite/main.html")


def requisite(request):
    if request.session['position_id'] != 2:
        return redirect('authorization')
    output = Requisite.objects.all()
    typeFilter = RequisiteTypeFilter(request.GET, queryset=output)
    output = typeFilter.qs
    return render(request, 'Requisite/requisite.html', {'requisite': output, 'typeFilter': typeFilter})


def requisite_history(request):
    if request.session['position_id'] != 2:
        return redirect('authorization')
    output = RequisiteHistory.objects.all()
<<<<<<< HEAD
    requisiteFilter = RequisiteFilter(request.GET, queryset=output)
    output = requisiteFilter.qs
    return render(request, 'Requisite/requisite_history.html', {'requisite': output,
                                                                'requisiteFilter': requisiteFilter})
=======
    return render(request, 'Requisite/requisite_history.html', {'requisite': output})
>>>>>>> 2e166d30e963d225d123d3ad03c11980f04e4c4d


def requisite_poster_role(request):
    if request.session['position_id'] != 2:
        return redirect('authorization')
    output = RequisitePosterRole.objects.all()
<<<<<<< HEAD
    requisiteFilter = RequisiteFilter(request.GET, queryset=output)
    output = requisiteFilter.qs
    return render(request, 'Requisite/requisite_poster_role.html', {'requisite': output,
                                                                    'requisiteFilter': requisiteFilter})


def create_requisite_type(request):
    if request.session['position_id'] != 2:
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
        'error': error
    }
    return render(request, 'requisite/create_requisite_type.html', data)


def create_requisite(request):
    if request.session['position_id'] != 2:
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
        'error': error
    }
    return render(request, 'requisite/create_requisite.html', data)


def create_requisite_his(request):
    if request.session['position_id'] != 2:
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
    if request.session['position_id'] != 2:
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


def sort_requisite_asc(request):
    requisite = RequisiteHistory.objects.all()
    requisite = requisite.order_by('price')
    return render(request, "Requisite/requisite_history.html", {"requisite": requisite})


def sort_requisite_desc(request):
    requisite = RequisiteHistory.objects.all()
    requisite = requisite.order_by('-price')
    return render(request, "Requisite/requisite_history.html", {"requisite": requisite})
=======
    return render(request, 'Requisite/requisite_poster_role.html', {'requisite': output})
>>>>>>> 2e166d30e963d225d123d3ad03c11980f04e4c4d
