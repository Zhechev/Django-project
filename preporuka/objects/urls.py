from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:pk>/', views.UserObjectsView.as_view(), name='user-objects'),
    path('add/', views.add_object, name='add-object'),
    path('<int:pk>/', views.show_object, name='show-object'),
    path('all/<int:category_id>/', views.show_all_objects, name="show-all-objects"),
]