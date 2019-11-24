from django.shortcuts import render
from django.http import JsonResponse
from nearby.models import Place, User ,PlaceUser
from nearby.input import Places
from . import place_nearby
from django.core import serializers
import geocoder
import time
from django_globals import globals

import socket


def compute_rank_point(visited_count, count_time_avg):
    rank = visited_count*0.8+count_time_avg*0.2
    return rank

def get_user_location2():

    my_location = geocoder.ip('me')
    get_user_location2.user_lat = float(my_location.latlng[0])
    get_user_location2.user_lon = float(my_location.latlng[1])

    print(get_user_location2.user_lat)
    print(get_user_location2.user_lon)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 80))
    print("Your Computer IP Address is: " + s.getsockname()[0])
    get_user_location2.lo = s.getsockname()[0]


def get_user_location(request):

    my_location = geocoder.ip('me')
    
    # get_user_location.user_lat = 18.291952 
    # get_user_location.user_lon = 99.493211
    get_user_location.user_lat = request.POST.get('lat')
    get_user_location.user_lon = request.POST.get('long')

    if get_user_location.user_lat is None or get_user_location.user_lon is None:
        my_location = geocoder.ip('me')
        get_user_location.user_lat = float(my_location.latlng[0])
        get_user_location.user_lon = float(my_location.latlng[1])
    else:
        get_user_location.user_lat = float(request.POST.get('lat'))
        get_user_location.user_lon = float(request.POST.get('long'))

    print(get_user_location.user_lat)
    print(get_user_location.user_lon)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 80))
    print("Your Computer IP Address is: " + s.getsockname()[0])
    get_user_location.lo = s.getsockname()[0]

    context = {
        'ip': get_user_location.lo
    }
    return render(request, template_name="nearby/location.html", context=context)


def search(request):
    global place_type
    if request.POST.get('place_type') is not None:
        place_type = request.POST.get('place_type')
    print(place_type)
    return render(request, template_name='nearby/search.html')


count_time = 0
current_place = None
count_time_to_get_api = -1
place_type = "hospital"  # example
api_key = "AIzaSyBbq0VljhDuyG5TkqguBiL9Wnnq-_BTa1k"
get_user_location2()
place_api = place_nearby.places_nearby(get_user_location2.user_lat, get_user_location2.user_lon, place_type, api_key)
user = Places(get_user_location2.user_lat,get_user_location2.user_lon, place_api, get_user_location2.lo)

def index(request, type):
    global current_place
    global count_time
    global count_time_to_get_api
    global place_type
    global api_key
    global user
    global place_api
    context = dict()

    if type == 'nearby':
        type = None
    place_type= type
    print(place_type)
    print(str(count_time_to_get_api)+" count time to get api")
    print(str(count_time)+" count time")
    print(str(current_place)+" current place")
    # print(user.place_api)
    
  # outside the place
    if count_time_to_get_api == -1:
        count_time_to_get_api += 1
        get_user_location(request)
        print("first start")
        place_api = place_nearby.places_nearby(get_user_location.user_lat, get_user_location.user_lon, place_type, api_key)
        user = Places(get_user_location.user_lat,get_user_location.user_lon, place_api, get_user_location.lo)
        user.rank_place()

    if count_time_to_get_api == 6 :
        count_time_to_get_api = 0
        get_user_location(request)
        user.user_lat = get_user_location.user_lat
        user.user_lon = get_user_location.user_lon
        print("get new api at 1 min")
        user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)
        user.rank_place()

    # elif count_time != 0:
    else:
        print("count time api ++")
        count_time_to_get_api += 1
        get_user_location(request)
        user.user_lat = get_user_location.user_lat
        user.user_lon = get_user_location.user_lon

    # time.sleep(1)

    try:
        print("get user success")
        db = User.objects.get(ip=user.ip_id)  # get IP from User db
        uid = db.iduser
    except:
        print("create user")
        User.objects.create(ip=user.ip_id)  # save to db
        db = User.objects.get(ip=user.ip_id)
        uid = db.iduser

    if user.find_nearest_place() == current_place and user.find_nearest_place() != None:
        print("at some place")
        current_place = user.find_nearest_place()
        count_time += 1
        count_time_to_get_api = 0
        # if(count_time == 10):
        #     current_place = {'geometry': {'location': {'lat': 12.886, 'lng': 24.5906}},
        #               'name': 'nnnnn', }
        # time.sleep(1)
        context = {
        'place': user.place_api
        # 'place':place_api
        }
        # return render(request, template_name="nearby/location.html", context=context)
        # print(user)
        # user_show = serializers.serialize('json', [ user, ])
        # return JsonResponse(user_show, safe=False)
        return JsonResponse(context, safe=False)

    elif count_time >= 90:  # more than 15 mins #get data from db current place
        try:
            print("count time > 900 get all place")
            place_all = Place.objects.values_list('place_name', flat=True)
        except:
            print("count time > 900 get no place to get")
            place_all = []
        
        # pid = ""  # place id

        if current_place.get('name') in place_all:  # save new place to Place table
            print("place already saved")
            pid = Place.objects.get(place_name=current_place.get('name')).idplace

        else:
            print("create place")
            Place.objects.create(
                place_name=current_place.get('name'),
                latitude=current_place.get('geometry').get('location').get('lat'),
                longitude=current_place.get('geometry').get('location').get('lng'),
                image=current_place.get('image')
            )
            pid = Place.objects.get(place_name=current_place.get('name')).idplace



        try:
            print("update placeuser")
            place_user = PlaceUser.objects.all().filter(place_idplace=pid, user_iduser=uid)
            count_time_avg = (place_user[0].avg_spending_time * place_user[0].visit_count + place_user[0].avg_spending_time) / (place_user[0].visit_count + 1)
            visited_count = place_user[0].visit_count + 1
            rank_point = compute_rank_point(visited_count, count_time_avg)  # compute rank point

            new_pu = PlaceUser.objects.get(place_idplace=pid,user_iduser=uid)
            new_pu.visit_count=visited_count
            new_pu.avg_spending_time=count_time_avg
            new_pu.ranking=rank_point
            new_pu.save()

        except:
            print("create placeuser")
            new_pu = PlaceUser(
                place_idplace=Place.objects.get(idplace=pid),
                user_iduser=User.objects.get(iduser=uid),
                visit_count=1,
                avg_spending_time=count_time,
                ranking= compute_rank_point(1, count_time)
            )
            new_pu.save()

        count_time = 0
        visited_count = 0
        current_place = None

    elif count_time != 0:
        print("not in place")
        user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)
        count_time = 0

    

    
    current_place = user.find_nearest_place()
    context = {
        # 'place': user.place_api
        'place' : user.place_api
    }
    # print(user.places)

    # return render(request, template_name="nearby/location.html", context=context)
    # user_show = serializers.serialize('json', user)
    return JsonResponse(context, safe=False)