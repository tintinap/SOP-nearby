from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('location/', views.get_user_location, name='location'),
    path('search/', views.search, name='search')
]