from django.shortcuts import render
from django.http import JsonResponse
from nearby.models import Place, User ,PlaceUser
from nearby.input import Places
from . import place_nearby
from django.core import serializers
import geocoder
import time
# from django_globals import globals
import json
from background_task import background

import socket

count_time = 0
current_place = None
count_time_to_get_api = -1
place_type = ""  # example
previus_place_type = ""
api_key = "AIzaSyBbq0VljhDuyG5TkqguBiL9Wnnq-_BTa1k"
# get_user_location2()
# place_api = place_nearby.places_nearby(get_user_location2.user_lat, get_user_location2.user_lon, place_type, api_key)
# user = Places(get_user_location2.user_lat,get_user_location2.user_lon, place_api, get_user_location2.lo)
json_string = {}
lat = 0.0
lng = 0.0
index1 = 0

def update_lat_lng(request, lat, lng): #it should contain lat lng from request from frontend
    """
    Only update global variable of lat , lng and place_type
    """
    global lat
    global lng
    global place_type

    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    

# @background(schedule=5)
# def updateJSON():
#     """
#     update JSON from input and also run the business logic of service
#     """
#     global current_place
#     global count_time
#     global count_time_to_get_api
#     global previus_place_type
#     global api_key
#     global user
#     global place_api

#     global json_string
#     global place_type
#     global lat
#     global lng
#     global index1

#     lati = lat
#     long = lng
#     print(str(index1)+"index")
#     print(place_type)
#     print(previus_place_type)
#     print(lati, long)
#     print(str(count_time_to_get_api)+" count time to get api")
#     print(str(count_time)+" count time")
#     print(str(current_place)+" current place")
    
#   # outside the place
#     if previus_place_type != place_type and (place_type != None or place_type != ""):
#         previus_place_type = place_type
#         print("place_type change")
#         # return render(request, 
#         #         template_name="nearby/location.html"
#         #     )
#     else:
#         place_type = previus_place_type

#     if index1 == 1:
#         index1 += 1
#         # count_time_to_get_api += 1
#         # get_user_location()
#         print("first start")
#         print(place_type+","+lati+","+long)
#         user.user_lat = lati
#         user.user_lon = long
#         place_api = place_nearby.places_nearby(lati, long, place_type, api_key)
#         # user = Places(lati,long, place_api, get_user_location.lo)

#         user.rank_place()
    
#     if count_time_to_get_api == -1:
#         count_time_to_get_api += 1
#         get_user_location()
#         print("first start")
#         place_api = place_nearby.places_nearby(lati, long, place_type, api_key)
#         user = Places(lati,long, place_api, get_user_location.lo)
#         user.rank_place()

#     print(user.ip_id)

#     if count_time_to_get_api == 6 :
#         count_time_to_get_api = 0
#         # get_user_location(request)
#         user.user_lat = lati
#         user.user_lon = long
#         # user.user_lat = get_user_location.user_lat
#         # user.user_lon = get_user_location.user_lon
#         print("get new api at 1 min")
#         user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)
#         user.rank_place()

#     else:
#         print("count time api ++")
#         count_time_to_get_api += 1
#         user.user_lat = lati
#         user.user_lon = long
#         # get_user_location(request)
#         # user.user_lat = get_user_location.user_lat
#         # user.user_lon = get_user_location.user_lon

#     try:
#         print("get user success")
#         db = User.objects.get(ip=user.ip_id)  # get IP from User db
#         uid = db.iduser
#     except:
#         print("create user")
#         User.objects.create(ip=user.ip_id)  # save to db
#         db = User.objects.get(ip=user.ip_id)
#         uid = db.iduser

#     if user.find_nearest_place() == current_place and user.find_nearest_place() != None:
#         print("at some place")
#         current_place = user.find_nearest_place()
#         count_time += 1
#         count_time_to_get_api = 0
#         context = {
#             'place': user.place_api
#         }
#         print('hi')
#         json_string = json.dumps(context)
#         # return json_string #return 1

#     elif count_time >= 90:  # more than 15 mins #get data from db current place
#         try:
#             print("count time > 900 get all place")
#             place_all = Place.objects.values_list('place_name', flat=True)
#         except:
#             print("count time > 900 get no place to get")
#             place_all = []

#         if current_place.get('name') in place_all:  # save new place to Place table
#             print("place already saved")
#             pid = Place.objects.get(place_name=current_place.get('name')).idplace

#         else:
#             print("create place")
#             Place.objects.create(
#                 place_name=current_place.get('name'),
#                 latitude=current_place.get('geometry').get('location').get('lat'),
#                 longitude=current_place.get('geometry').get('location').get('lng'),
#                 image=current_place.get('image')
#             )
#             pid = Place.objects.get(place_name=current_place.get('name')).idplace



#         try:
#             print("update placeuser")
#             place_user = PlaceUser.objects.all().filter(place_idplace=pid, user_iduser=uid)
#             count_time_avg = (place_user[0].avg_spending_time * place_user[0].visit_count + place_user[0].avg_spending_time) / (place_user[0].visit_count + 1)
#             visited_count = place_user[0].visit_count + 1
#             rank_point = compute_rank_point(visited_count, count_time_avg)  # compute rank point

#             new_pu = PlaceUser.objects.get(place_idplace=pid,user_iduser=uid)
#             new_pu.visit_count=visited_count
#             new_pu.avg_spending_time=count_time_avg
#             new_pu.ranking=rank_point
#             new_pu.save()

#         except:
#             print("create placeuser")
#             new_pu = PlaceUser(
#                 place_idplace=Place.objects.get(idplace=pid),
#                 user_iduser=User.objects.get(iduser=uid),
#                 visit_count=1,
#                 avg_spending_time=count_time,
#                 ranking= compute_rank_point(1, count_time)
#             )
#             new_pu.save()

#         count_time = 0
#         visited_count = 0
#         current_place = None

#     elif count_time != 0:
#         print("not in place")
#         user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)
#         count_time = 0

#     current_place = user.find_nearest_place()
#     context = {
#         # 'place': user.place_api
#         'place': user.place_api
#     }
#     print('hi2')
#     print(user.place_api)
#     json_string = json.dumps(context)
#     # return json_string #return 2

def compute_rank_point(visited_count, count_time_avg):
    rank = visited_count*0.8+count_time_avg*0.2
    return rank


def get_user_location():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 80))
    print("Your Computer IP Address is: " + s.getsockname()[0])
    get_user_location.lo = s.getsockname()[0]

c = 0
@background(schedule=5)
def hello():
    # global c
    print('hello'+str(c))


def search(request):
    global place_type
    global c
    print('SEARCH')

    c += 1
    hello(repeat=5)
    print(c)
    return render(request, template_name='nearby/search.html')

def index(request,  lati, long, type=None):
    global current_place
    global count_time
    global count_time_to_get_api
    global place_type
    global previus_place_type
    global api_key
    global user
    global place_api
    global json_string
    global lat
    global lng
    global index1

    lat = float(lati)
    lng = float(long)

    place_type= type
    print(place_type)
    print(str(lati)+','+str(long)+'-->from url')
    print(str(lat)+','+str(lng)+'-->global')
    print(str(count_time_to_get_api)+" count time to get api")
    print(str(count_time)+" count time")
    print(str(current_place)+" current place")

    if previus_place_type != place_type and place_type != None:
        previus_place_type = place_type
        index1 +=1
        print("place_type change")

    else:
        place_type = previus_place_type
        print(previus_place_type)

    updateJSON(repeat=5)
        
    return JsonResponse(json_string, safe=False)

   