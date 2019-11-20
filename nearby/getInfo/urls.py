from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.get_location, name='location'),
    path('location2/', views.location, name='location2'),
]
