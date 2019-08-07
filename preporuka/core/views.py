from django.shortcuts import render
from django.views import generic


class HomePageView(generic.View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)
