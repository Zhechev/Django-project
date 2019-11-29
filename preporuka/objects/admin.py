from django.contrib import admin
from .models import Object, Comment, Restaurant, SportFitness, CarService, BeautySalon, FastFood, CarWash, Fun, Other, City

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(SportFitness)
admin.site.register(CarService)
admin.site.register(BeautySalon)
admin.site.register(FastFood)
admin.site.register(CarWash)
admin.site.register(Fun)
admin.site.register(Other)
admin.site.register(City)


class CommentScreenAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'object')

admin.site.register(Comment, CommentScreenAdmin)