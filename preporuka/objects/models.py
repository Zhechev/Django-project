from django.db import models
from users.models import ProfileUser
from django.utils import timezone
from polymorphic.models import PolymorphicModel

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Object(PolymorphicModel):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, db_column='author')
    title = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=100, default='')
    site = models.CharField(max_length=100, default='')
    facebook = models.CharField(max_length=100, default='')
    instagram = models.CharField(max_length=100, default='')
    content = models.TextField()
    rating = models.IntegerField(default=10)
    created_date = models.DateTimeField(default=timezone.now)
    approved_object = models.BooleanField(default=False)
    admin_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}" 


class Restaurant(Object):
    seats = models.IntegerField()
    bulgarian_kitchen = models.BooleanField(default=False)
    italian_kitchen = models.BooleanField(default=False)
    french_kitchen = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='restaurants')
    category_bg_name = models.CharField(max_length=100, default='Ресторанти')
    bg_name = models.CharField(max_length=100, default='Ресторант')
    is_garden = models.BooleanField(default=False)
    is_playground = models.BooleanField(default=False)


class SportFitness(Object):
    is_fitness_trainer = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='sportfitness')
    category_bg_name = models.CharField(max_length=100, default='Спорт и фитнес')
    bg_name = models.CharField(max_length=100, default='Спорт и фитнес')


class CarService(Object):
    is_parts_clients = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='carservice')
    category_bg_name = models.CharField(max_length=100, default='Автосервизи')
    bg_name = models.CharField(max_length=100, default='Автосервиз')


class BeautySalon(Object):
    is_hair_salon = models.BooleanField(default=False)
    is_laser_epilation = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='beautysalon')
    category_bg_name = models.CharField(max_length=100, default='Салони за красота')
    bg_name = models.CharField(max_length=100, default='Салон за красота')


class FastFood(Object):
    is_pizza = models.BooleanField(default=False)
    is_duner = models.BooleanField(default=False)
    is_seats = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='fastfood')
    category_bg_name = models.CharField(max_length=100, default='Бързо хранене')
    bg_name = models.CharField(max_length=100, default='Бързо хранене')


class CarWash(Object):
    is_external_cleaning = models.BooleanField(default=False)
    is_internal_cleaning = models.BooleanField(default=False)
    is_engine_cleaning = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='carwash')
    category_bg_name = models.CharField(max_length=100, default='Автомивка')
    bg_name = models.CharField(max_length=100, default='Автомивка')


class Fun(Object):
    is_working_weekend = models.BooleanField(default=False)
    is_kids_suitable = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='fun')
    category_bg_name = models.CharField(max_length=100, default='Забавление')
    bg_name = models.CharField(max_length=100, default='Забавление')


class Other(Object):
    is_working_weekend = models.BooleanField(default=False)
    category_en_name = models.CharField(max_length=100, default='other')
    category_bg_name = models.CharField(max_length=100, default='Други')
    bg_name = models.CharField(max_length=100, default='Други')


class Comment(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, db_column='author')
    content = models.TextField()
    rating = models.TextField()
    approved_object = models.BooleanField(default=False)
    admin_seen = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content}"


class Images(models.Model):
    file = models.FileField(upload_to='attachments')