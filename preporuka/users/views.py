from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def redirect_to_user_profile(request):
    url = f'/users/profile/{request.user.id}'
    return HttpResponseRedirect(redirect_to=url)


class UserProfileView(generic.DetailView):
    model = User
    template_name = 'user_profile.html'