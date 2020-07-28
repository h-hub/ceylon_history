from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from event.models import Event


def index(request):
    events = Event.objects.all()

    context = {
        'events': events,
        'end': range(2500)
    }

    return render(request, 'template/home.html', context)


def getEvent(request):
    year = request.GET.get('year', None)
    events = []
    events = Event.objects.get(date__year=year)


    data = {
        'events': events
    }

    return JsonResponse(data)
