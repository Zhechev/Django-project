from django.urls import path, re_path
from . import views

urlpatterns = [
    path('user/<int:pk>/', views.UserObjectsView.as_view(), name='user-objects'),
    path('add/<str:category>/', views.add_object, name='add-object'),
    path('<str:category>/<int:pk>/<int:page_num>/', views.show_object, name='show-object'),
    #path('all/<str:category>/<int:page_num>/', views.show_all_objects, name="show-all-objects"),
    re_path(r'all/(?P<category>\w+)/(?P<page_num>\w+)/?/(?P<city>\d+)?', views.show_all_objects, name="show-all-objects"),
]