from django.shortcuts import render, redirect
from django.views import generic
from objects.models import Object, ProfileUser, Comment, Restaurant, SportFitness, CarService, BeautySalon, FastFood, CarWash, Fun, Other
from .forms import ObjectForm, CommentForm
from django.contrib import messages
from django.db.models import Avg
import sys

class AllObjects(generic.ListView):
    queryset = Object.objects.all()
    template_name = 'show_all_objects.html'

class UserObjectsView(generic.ListView):
    template_name = 'user_objects.html'

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Object.objects.filter(author_id = user_id)

def add_object(request):
    if not request.user.is_authenticated:
        messages.info(request, 'За да добавите нов Обект, трябва да сте регистриран потребител!')
        return redirect('account_login')
    form = ObjectForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = ProfileUser.objects.get(user=request.user)
        obj.save()
        messages.success(request, 'Успешно добавихте нов Обект, може да видите вашите обекти във вашия профил!')
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, "add_object.html", context)

def show_object(request, pk):
    obj = Object.objects.get(id=pk)

    if request.method == 'POST':
        user = request.user
        author = ProfileUser.objects.get(user=user)
        comment = Comment()
        comment.object = obj
        comment.author = author
        comment.content = request.POST.get('content')
        comment.rating = request.POST.get('rating')
        comment.save()

    form = CommentForm()
    reviews_count = Comment.objects.filter(object_id=pk).count()
    rating = Comment.objects.filter(object_id=pk).aggregate(Avg('rating'))['rating__avg']

    context = {
        'form': form,
        'object': obj,
        'reviews_count': reviews_count,
        'rating': rating
    }

    return render(request, "show_object.html", context)

def show_all_objects(request, category):
    objects = eval(category).objects.all()
    context = {
        'object_list': objects,
    }

    return render(request, 'show_all_objects.html', context)