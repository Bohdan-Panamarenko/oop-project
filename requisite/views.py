from django.shortcuts import render
from .models import Requisite, RequisiteHistory, RequisitePosterRole


def main(request):
    return render(request, "Requisite/main.html")


def requisite(request):
    output = Requisite.objects.all()
    return render(request, 'Requisite/requisite.html', {'requisite': output})


def requisite_history(request):
    output = RequisiteHistory.objects.all()
    return render(request, 'Requisite/requisite_history.html', {'requisite': output})


def requisite_poster_role(request):
    output = RequisitePosterRole.objects.all()
    return render(request, 'Requisite/requisite_poster_role.html', {'requisite': output})
