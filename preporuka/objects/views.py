from django.shortcuts import render, redirect
from django.views import generic
from objects.models import Object, ProfileUser
from .forms import ObjectForm
from django.contrib import messages


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