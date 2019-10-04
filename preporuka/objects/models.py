from django.db import models
from users.models import ProfileUser
from django.utils import timezone

# Create your models here.

class Object(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    content = models.TextField()
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
    is_garden = models.BooleanField(default=False)
    is_playground = models.BooleanField(default=False)


class SportFitness(Object):
    is_fitness_trainer = models.BooleanField(default=False)


class CarService(Object):
    is_parts_clients = models.BooleanField(default=False)


class BeautySalon(Object):
    is_hair_salon = models.BooleanField(default=False)
    is_laser_epilation = models.BooleanField(default=False)


class FastFood(Object):
    is_pizza = models.BooleanField(default=False)
    is_duner = models.BooleanField(default=False)
    is_seats = models.BooleanField(default=False)


class CarWash(Object):
    is_external_cleaning = models.BooleanField(default=False)
    is_internal_cleaning = models.BooleanField(default=False)
    is_engine_cleaning = models.BooleanField(default=False)


class Fun(Object):
    is_working_weekend = models.BooleanField(default=False)
    is_kids_suitable = models.BooleanField(default=False)


class Other(Object):
    is_working_weekend = models.BooleanField(default=False)


class Comment(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.content}"