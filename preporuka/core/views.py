from django.shortcuts import render, redirect
from objects.models import City, Object, Restaurant, FastFood, SportFitness, CarService, BeautySalon, CarWash, Fun, Other
from django.core.paginator import Paginator


def show_home_page(request):
    cities = City.objects.all()
    objects = Object.objects.all()
    restaurant_count = len(Restaurant.objects.all())
    sportfitness_count = len(SportFitness.objects.all())
    carsevice_count = len(CarService.objects.all())
    beauty_salon_count = len(BeautySalon.objects.all())
    fastfood_count = len(FastFood.objects.all())
    car_wash_count = len(CarWash.objects.all())
    fun_count = len(Fun.objects.all())
    other_count = len(Other.objects.all())

    context = {
        'objects': objects,
        'cities': cities,
        'restaurant_count': restaurant_count,
        'sportfitness_count': sportfitness_count,
        'carsevice_count': carsevice_count,
        'beauty_salon_count': beauty_salon_count,
        'fastfood_count': fastfood_count,
        'car_wash_count': car_wash_count,
        'fun_count': fun_count,
        'other_count': other_count,
    }

    return render(request, "home.html", context)

def search_objects(request):

    category = request.POST.get('category')
    city = request.POST.get('city')

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


    objects = Object.objects.instance_of(params_map.get(category)).filter(city=city)

    if request.POST.get('title'):
        objects = objects.filter(title__icontains=request.POST.get('title'))


    print(objects)

    if city is not None:
        objects = objects.filter(city=city)

    paginator = Paginator(objects, 2)
    objects = paginator.get_page(1)

    context = {
        'objects': objects,
        'category': category,
        'page_num': 1,
    }

    return render(request, 'show_all_objects.html', context)