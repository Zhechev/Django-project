from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', include('allauth.urls')),
    path('profile/', views.redirect_to_user_profile, name='redirect-user-profile'),
    re_path('profile/(?P<pk>\d+)/', views.UserProfileView.as_view(), name='user-profile'),
]
