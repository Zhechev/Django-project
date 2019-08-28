from django.shortcuts import render
from django.views import generic
from objects.models import Object


class HomePageView(generic.ListView):
    queryset = Object.objects.all()
    template_name = 'home.html'