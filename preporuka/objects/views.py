from django.shortcuts import render, redirect
from django.views import generic
from objects.models import Object, ProfileUser, Comment, Restaurant, SportFitness, CarService, BeautySalon, FastFood, CarWash, Fun, Other
from .forms import RestaurantForm, SportFitnessForm, BeautySalonForm, CarServiceForm, CarWashForm, FastFoodForm, FunForm, OtherForm, CommentForm, UploadForm
from django.contrib import messages
from django.db.models import Avg
from django.apps import apps
from django.core.paginator import Paginator
from django.http import JsonResponse

class AllObjects(generic.ListView):
    queryset = Object.objects.all()
    template_name = 'show_all_objects.html'

class UserObjectsView(generic.ListView):
    template_name = 'user_objects.html'

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Object.objects.filter(author = user_id)

def add_object(request, category):
    if not request.user.is_authenticated:
        messages.info(request, 'За да добавите нов Обект, трябва да сте регистриран потребител!')
        return redirect('account_login')


    FunForm(request.POST or None)

    params_map = {
        'restaurants': RestaurantForm(request.POST or None),
        'sportfitness': SportFitnessForm(request.POST or None),
        'carservice': CarServiceForm(request.POST or None),
        'beautysalon': BeautySalonForm(request.POST or None),
        'fastfood': FastFoodForm(request.POST or None),
        'carwash': CarWashForm(request.POST or None),
        'fun': FunForm(request.POST or None),
        'other': OtherForm(request.POST or None),
    }

    form = params_map[category]

    upload_form = UploadForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = ProfileUser.objects.get(user=request.user)
        obj.save()
        messages.success(request, 'Успешно добавихте нов Обект, може да видите вашите обекти във вашия профил!')
        return redirect('home')


    context = {
        'form': form,
        'upload_form': upload_form
    }

    return render(request, "add_object.html", context)

def show_object(request, category, pk, page_num):
    categories = {'restaurants' : 'Restaurant', 'sportfitness' : 'SportFitness', 'carservice' : 'CarService', 'beautysalon' : 'BeautySalon', 'fastfood' : 'FastFood', 'carwash' : 'CarWash', 'fun' : 'Fun', 'other' : 'Other'}
    obj = apps.get_model('objects', categories[category]).objects.get(id=pk)

    if request.method == 'POST':
        data = {'error': False, 'error_message': ''}
        user = request.user
        author = ProfileUser.objects.get(user=user)
        comment = Comment()
        object = Object.objects.get(id=pk)
        comment.object = obj
        comment.author = author
        comment.content = request.POST.get('content')
        comment.rating = request.POST.get('rating')
        rating = Comment.objects.filter(object_id=pk).aggregate(Avg('rating'))['rating__avg']
        object.rating = rating
        data['rating'] = rating
        comment.save()
        object.save()

        return JsonResponse(data)

    form = CommentForm()
    reviews_count = Comment.objects.filter(object_id=pk).count()
    rating = Comment.objects.filter(object_id=pk).aggregate(Avg('rating'))['rating__avg']
    comments_list = Comment.objects.all()
    paginator = Paginator(comments_list, 2)
    comments = paginator.get_page(page_num)

    context = {
        'form': form,
        'object': obj,
        'reviews_count': reviews_count,
        'rating': rating,
        'category': category,
        'comments': comments,
        'page_num': page_num,
    }

    return render(request, "show_object.html", context)

def show_all_objects(request, category, page_num, city=None):
    params_map = {
        'restaurants': Restaurant,
        'sportfitness': SportFitness,
        'carservice': CarService,
        'beautysalon': BeautySalon,
        'fastfood': FastFood,
        'carwash': CarWash,
        'fun': Fun,
        'other': Other,
    }

    objects = Object.objects.instance_of(params_map.get(category))

    print(objects)

    if city is not None:
        objects = objects.filter(city=city)

    paginator = Paginator(objects, 2)
    objects = paginator.get_page(page_num)

    context = {
        'objects': objects,
        'category': category,
        'page_num': page_num,
    }

    return render(request, 'show_all_objects.html', context)

def search_objects(request):
    show_all_objects(request, request.POST.get('category'), 'тест', request.POST.get('city'))