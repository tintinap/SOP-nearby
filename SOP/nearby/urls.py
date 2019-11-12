from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('location/', views.get_user_location, name='location')
]