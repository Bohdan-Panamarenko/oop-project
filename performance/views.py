from django.shortcuts import render, redirect

from .forms import PerformanceForm, PerformanceOnGoingForm
from .models import Performance, Poster, Tier
from django.views.generic import DetailView, UpdateView, DeleteView
from ticketStore.models import Ticket


def main(request):
    if request.session['position'] != 2 and request.session['position'] != 6:
        return redirect('authorization')
    return render(request, 'performance/main.html', {'data': request.session['position']})


def performance(request):
    if request.session['position'] != 2 and request.session['position'] != 6:
        return redirect('authorization')
    performances = Performance.objects.all()
    return render(request, 'performance/performance.html', {'performances': performances, 'data': request.session['position']})


def sort_performance(request, pk):
    if request.session['position'] != 2 and request.session['position'] != 6:
        return redirect('authorization')
    performances = Performance.objects.all()
    if pk == 1:
        performances = performances.order_by('name')
    elif pk == 2:
        performances = performances.order_by('price')
    elif pk == 3:
        performances = performances.order_by('author')
    elif pk == 4:
        performances = performances.order_by('name').reverse()
    elif pk == 5:
        performances = performances.order_by('price').reverse()
    elif pk == 6:
        performances = performances.order_by('author').reverse()

    return render(request, "performance/performance.html", {"performances": performances, 'data': request.session['position']})


def create_performance(request):
    if request.session['position'] != 2 and request.session['position'] != 6:
        return redirect('authorization')
    form = PerformanceForm()
    error = ''
    if request.method == "POST":
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'performance/create_performance.html', data)


class PerformanceDetailView(DetailView):
    model = Performance
    template_name = 'performance/performance_info.html'
    context_object_name = 'performance'


class PerformanceUpdateView(UpdateView):
    model = Performance
    template_name = 'performance/performance_update.html'
    success_url = '/performance/performance'
    form_class = PerformanceForm


class PerformanceDeleteView(DeleteView):
    model = Performance
    template_name = 'performance/performance_delete.html'
    success_url = '/performance/performance'


def performance_on_going(request):
    if request.session['position'] != 2 and request.session['position'] != 6:
        return redirect('authorization')
    poster = Poster.objects.all()
    return render(request, 'performance/performance_on_going.html', {'poster': poster, 'data': request.session['position']})


def sort_performance_on_going(request, pk):
    if request.session['position'] != 2 and request.session['position'] != 6:
        return redirect('authorization')
    posters = Poster.objects.all()
    if pk == 1:
        posters = posters.order_by('date')
    elif pk == 2:
        posters = posters.order_by('performance_id__name')
    elif pk == 3:
        posters = posters.order_by('performance_id__price')
    elif pk == 4:
        posters = posters.order_by('performance_id__author')
    elif pk == 5:
        posters = posters.order_by('date').reverse()
    elif pk == 6:
        posters = posters.order_by('performance_id__name').reverse()
    elif pk == 7:
        posters = posters.order_by('performance_id__price').reverse()
    elif pk == 8:
        posters = posters.order_by('performance_id__author').reverse()

    return render(request, "performance/performance_on_going.html", {"poster": posters, 'data': request.session['position']})


def create_tickets(poster: Poster):
    tiers = Tier.objects.filter(hall_id=poster.hall_id)
    i = 1

    for tier in tiers:
        for seat in range(1, tier.number_of_seats + 1):
            Ticket(
                price=poster.performance_id.price,
                place=i,
                availability=True,
                poster_id=poster,
                tier_id=tier
            ).save()
            i += 1


def create_performance_on_going(request):
    if request.session['position'] != 2 and request.session['position'] != 6:
        return redirect('authorization')
    form = PerformanceOnGoingForm()
    error = ''
    if request.method == "POST":
        form = PerformanceOnGoingForm(request.POST)
        if form.is_valid():
            poster = form.save()
            create_tickets(poster)
            return redirect('performance_on_going')
        else:
            error = 'Wrong values!'

    data = {
        'form': form,
        'error': error,
        'data': request.session['position']
    }
    return render(request, 'performance/create_performance_on_going.html', data)


class PerformanceOnGoingDetailView(DetailView):
    model = Poster
    template_name = 'performance/performance_on_going_info.html'
    context_object_name = 'performance_on_going'


class PerformanceOnGoingUpdateView(UpdateView):
    model = Poster
    template_name = 'performance/performance_on_going_update.html'
    success_url = '/performances/performance_on_going'
    form_class = PerformanceOnGoingForm


class PerformanceOnGoingDeleteView(DeleteView):
    model = Poster
    template_name = 'performance/performance_on_going_delete.html'
    success_url = '/performances/performance_on_going'


