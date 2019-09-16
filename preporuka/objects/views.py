from django.shortcuts import render, redirect
from django.views import generic
from objects.models import Object, ProfileUser
from .forms import ObjectForm, CommentForm
from django.contrib import messages

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
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.object = obj
        user = request.user
        author = ProfileUser.objects.get(user=user)
        comment.author = author
        comment.save()
        form = CommentForm()
        messages.success(request, 'Успешно добавихте нов коментар!')
        return redirect(request.path_info)

    context = {
        'form': form,
        'object': obj,
    }

    return render(request, "show_object.html", context)

def show_all_objects(request):
    objects = Object.objects.all()
    context = {
        'object_list': objects,
    }

    return render(request, 'show_all_objects.html', context)



#
# def add_comment_to_object(request, pk):
#     if not request.user.is_authenticated:
#         messages.info(request, 'За да добавите нов коментар, трябва да сте регистриран потребител!')
#         return redirect('account_login')
#     obj = Object.objects.get(id=pk)
#     form = CommentForm(request.POST or None)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.object = obj
#         user = request.user
#         author = ProfileUser.objects.get(user=user)
#         comment.author = author
#         comment.save()
#         return redirect('home')
#     else:
#         form = CommentForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'add_comment.html', context)