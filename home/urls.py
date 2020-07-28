from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('event', views.getEvent, name='events'),
]