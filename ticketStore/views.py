from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Ticket, Ticket_ordered, Order
from performance.models import *
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from django.views.generic.base import View
from .forms import OrderForm
from .filters import PerformanceFilter, PosterFilter
import numpy as np
from datetime import datetime, timedelta, date
import pytz
utc = pytz.UTC
# Create your views here.
global ticket_order
tickets_order = []
global ticket_order_for_order
ticket_order_for_order = []
global tick
globals()['tick'] = 0
global order_price
globals()['order_price'] = 0


def ticketStore_main(request, pk=None):
    if pk == 'cancel':
        tickets_const = Ticket.objects.order_by('place')
        numpy_array = np.array(tickets_order)
        transpose = numpy_array.T
        tickets_order_output = transpose.tolist()
        for poster_el in tickets_order_output[1]:
            for place_el in tickets_order_output[2]:
                tickets_const.filter(place=place_el, poster_id_id__performance_id_id__name=poster_el).update(availability=1)
        tickets_order.clear()
        globals()['tick'] = 0
        globals()['order_price'] = 0
    poster = Poster.objects.order_by('id')
    myFilter = PosterFilter(request.GET, queryset=poster)
    poster = myFilter.qs
    return render(request, 'ticketStore/ticketStore_main.html', {'poster': poster, 'myFilter': myFilter})


def ticketStore_hot(request):
    now = datetime.now()
    date_today = now.strftime("%Y-%m-%d %H:%M")
    poster = Poster.objects.order_by('id')
    hot_posters_id = []
    for p in poster:
        now_time = now.replace(tzinfo=utc)
        p_time = p.date.replace(tzinfo=utc)
        if now_time < p_time - timedelta(days=7):
            hot_posters_id.append(p.id)
    return render(request, 'ticketStore/ticketStore_hot.html', {'poster': poster, 'date_today': date_today,
                                                                'hot_posters_id': hot_posters_id})


def ticketStore_performance(request, pk=None):
    tickets_const = Ticket.objects.order_by('place')
    return render(request, 'ticketStore/ticketStore_performance.html', {'tickets': tickets_const, 'pk': pk,
                                                                        'tickets_order': tickets_order,
                                                                        'tick': tick, 'order_price': order_price})


def ticketStore_order(request, pk, pkt=None):
    tickets_const = Ticket.objects.order_by('place')
    performances = Performance.objects.order_by('id')
    for el in tickets_const:
        if el.place == pkt and el.poster_id_id == pk:
            tickets_const.filter(place=pkt, poster_id_id=pk).update(availability=0)
            performance = performances.get(id=pk).name
            if not [pk, performance, pkt, 1] in tickets_order:
                ticket_order_for_order.append([pk, pkt])
                tickets_order.append([pk, performance, pkt, 1])
                globals()['tick'] += 1
                globals()['order_price'] += tickets_const.get(place=pkt, poster_id_id=pk).price
    return render(request, 'ticketStore/ticketStore_order.html', {'tickets': tickets_const, 'pk': pk, 'pkt': pkt,
                                                                  'tickets_order': tickets_order,
                                                                  'tick': tick, 'order_price': order_price})


def ticketStore_cancel(request, pk, pkt):
    if int(len(tickets_order)) == 1:
        tickets_const = Ticket.objects.order_by('place')
        performances = Performance.objects.order_by('id')
        tickets_const.filter(place=pkt, poster_id_id=pk).update(availability=1)
        performance = performances.get(id=pk).name
        if [pk, performance, pkt, 1] in tickets_order:
            ticket_order_for_order.remove([pk, pkt])
            tickets_order.remove([pk, performance, pkt, 1])
            globals()['tick'] -= 1
            globals()['order_price'] -= tickets_const.get(place=pkt, poster_id_id=pk).price
        return ticketStore_main(request)
    else:
        tickets_const = Ticket.objects.order_by('place')
        performances = Performance.objects.order_by('id')
        tickets_const.filter(place=pkt, poster_id_id=pk).update(availability=1)
        performance = performances.get(id=pk).name
        if [pk, performance, pkt, 1] in tickets_order:
            ticket_order_for_order.remove([pk, pkt])
            tickets_order.remove([pk, performance, pkt, 1])
            globals()['tick'] -= 1
            globals()['order_price'] -= tickets_const.get(place=pkt, poster_id_id=pk).price
        return ticketStore_form(request)


def ticketStore_form(request):
    error = ''
    tickets_const = Ticket.objects.all()
    numpy_array0 = np.array(ticket_order_for_order)
    transpose0 = numpy_array0.T
    ticket_order_for_order_list = transpose0.tolist()
    numpy_array = np.array(tickets_order)
    transpose = numpy_array.T
    tickets_order_output = transpose.tolist()
    tickets_order_output_numpy_array = numpy_array.tolist()
    today = date.today()
    date1 = today.strftime("%Y-%m-%d")
    posters_form = Poster.objects.order_by('id')
    range_order = len(tickets_order_output[0])
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            orders = Order.objects.order_by('-id')
            order = orders[0]
            Order.objects.filter(id=order.id).update(price=order_price)
            Order.objects.filter(id=order.id).update(date=date1)
            # [[1,1,1], [38,39,40], [1,1,1]]
            for i in range(len(tickets_order_output[1])):
                Ticket_ordered.objects.create(
                    order=order,
                    place=tickets_order_output[1][i],
                    poster_id_id=tickets_const.get(place=ticket_order_for_order_list[1][i],
                                                   poster_id_id=ticket_order_for_order_list[0][i]).poster_id_id,
                    price=tickets_const.get(place=ticket_order_for_order_list[1][i],
                                            poster_id_id=ticket_order_for_order_list[0][i]).price,
                    tier_id=tickets_const.get(place=ticket_order_for_order_list[1][i],
                                              poster_id_id=ticket_order_for_order_list[0][i]).tier_id_id)
            tickets_order.clear()
            globals()['tick'] = 0
            globals()['order_price'] = 0
            return redirect('ticketStore_main')
        else:
            error = 'Замовлення заповненно некоректно'
    form = OrderForm()
    return render(request, 'ticketStore/ticketStore_form.html',
                  {'form': form, 'error': error, 'tickets_order': tickets_order,
                   'order_price': order_price, 'posters_form': posters_form, 'tickets_order_output': tickets_order_output,
                   'range_order': range(int(range_order)), 'tickets_order_output_numpy_array': tickets_order_output_numpy_array})


def performance_filter(request, pk):
    poster = Poster.objects.all()
    if pk == 1:
        poster = poster.order_by('performance_id__price')
    if pk == 2:
        poster = poster.order_by('performance_id__duration')
    if pk == 3:
        poster = poster.order_by('date')
    myFilter = PosterFilter(request.GET, queryset=poster)
    poster = myFilter.qs
    return render(request, 'ticketStore/ticketStore_main.html', {'poster': poster, 'myFilter': myFilter})

def ordersList(request):
    if request.session['position'] != 2:
        return redirect('authorization')
    orders = Order.objects.all()
    return render(request, 'ticketStore/orders_list.html', {'orders': orders})


class OrdersDeleteView(DeleteView):
    model = Order
    template_name = 'ticketStore/orders_delete.html'
    success_url = '/orders/'