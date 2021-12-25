from django.shortcuts import render
from .models import Performance, Rating, Genre, Hall, Tier, Poster
from django.views.generic import ListView, DetailView, TemplateView


def main(request):
    return render(request, 'performance/main.html')


def performance(request):
    performances = Performance.objects.all()
    return render(request, 'performance/performance.html', {'performances': performances})


def sort_performance(request, pk):
    performances = Performance.objects.all()
    if pk == 1:
        performances = performances.order_by('name')
    elif pk == 2:
        performances = performances.order_by('price')
    elif pk == 3:
        performances = performances.order_by('author')

    return render(request, "performance/performance.html", {"performances": performances})


def performance_on_going(request):
    poster = Poster.objects.all()
    print(poster[0].date)
    return render(request, 'performance/performance_on_going.html', {'poster': poster})


def sort_performance_on_going(request, pk):
    posters = Poster.objects.all()
    if pk == 1:
        posters = posters.order_by('date')
    elif pk == 2:
        posters = posters.order_by('performance_id__name')
    elif pk == 3:
        posters = posters.order_by('performance_id__price')
    elif pk == 4:
        posters = posters.order_by('performance_id__author')

    return render(request, "performance/performance_on_going.html", {"poster": posters})

