from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from event.models import Event


def index(request):

    event = Event.objects.all()

    return render(request, 'template/home.html')