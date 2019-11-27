from django.urls import path
from . import views
urlpatterns = [
    path('nearby/<str:type>,<str:lati>,<str:long>', views.index, name='index'),
    # path('index/', views.index, name='index'),
    path('location/', views.index, name='location'),
    # path('location/', views.get_user_location, name='location'),
    path('search/', views.search, name='search'),
    path('update/<str:lati>,<str:long>', views.update_lat_lng, name='update')
]