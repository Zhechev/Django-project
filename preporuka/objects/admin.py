from django.contrib import admin
from .models import Object, Comment, Restaurant, SportFitness, CarService, BeautySalon, FastFood, CarWash, Fun, Other

# Register your models here.

admin.site.register(Comment)
admin.site.register(Restaurant)
admin.site.register(SportFitness)
admin.site.register(CarService)
admin.site.register(BeautySalon)
admin.site.register(FastFood)
admin.site.register(CarWash)
admin.site.register(Fun)
admin.site.register(Other)