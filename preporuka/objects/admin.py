from django.contrib import admin
from .models import Object, Comment, Category

# Register your models here.

admin.site.register(Object)
admin.site.register(Comment)
admin.site.register(Category)