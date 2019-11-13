from django.shortcuts import render
from django.http import JsonResponse
from nearby.models import Place, User ,PlaceUser
from nearby.input import Places
from . import place_nearby
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
    print("ooooooooo")
    print(request.GET.get('lat'))
    
    get_user_location.user_lat = 18.285952
    get_user_location.user_lon = 99.506082
    # get_user_location.user_lat = request.GET.get('lat')
    # get_user_location.user_lon = request.GET.get('long')

    # if get_user_location.user_lat is None or get_user_location.user_lon is None:
    #     my_location = geocoder.ip('me')
    #     get_user_location.user_lat = float(my_location.latlng[0])
    #     get_user_location.user_lon = float(my_location.latlng[1])
    # else:
    #     get_user_location.user_lat = float(request.GET.get('lat'))
    #     get_user_location.user_lon = float(request.GET.get('long'))

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


count_time = 0
current_place = None
count_time_to_get_api = -1
place_type = "hospital"  # example
api_key = "AIzaSyBbq0VljhDuyG5TkqguBiL9Wnnq-_BTa1k"
get_user_location2()
place_api = place_nearby.places_nearby(get_user_location2.user_lat, get_user_location2.user_lon, place_type, api_key)
user = Places(get_user_location2.user_lat,get_user_location2.user_lon, place_api, get_user_location2.lo)

def index(request):
    global current_place
    global count_time
    global count_time_to_get_api
    global place_type
    global api_key
    global user
    global place_api

    print(str(count_time_to_get_api)+" count time to get api")
    print(str(count_time)+" count time")
    print(str(current_place)+" current place")
    print(user)
    
  # outside the place
    if count_time_to_get_api == -1:
        count_time_to_get_api += 1
        get_user_location(request)
        print(1111111111111111)
        place_api = place_nearby.places_nearby(get_user_location.user_lat, get_user_location.user_lon, place_type, api_key)
        user = Places(get_user_location.user_lat,get_user_location.user_lon, place_api, get_user_location.lo)
        user.rank_place()

    if count_time_to_get_api == 60 :
        count_time_to_get_api = 0
        get_user_location(request)
        user.user_lat = get_user_location.user_lat
        user.user_lon = get_user_location.user_lon
        print(222222222222222)
        user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)
        user.rank_place()

    else:
        print(33333333333333)
        count_time_to_get_api += 1
        get_user_location(request)
        user.user_lat = get_user_location.user_lat
        user.user_lon = get_user_location.user_lon

    # time.sleep(1)

    try:
        print(4444444444444)
        db = User.objects.get(ip=user.ip_id)  # get IP from User db
    except:
        print(555555555555)
        User.objects.create(ip=user.ip_id)  # save to db
        db = User.objects.get(ip=user.ip_id)

    if user.find_nearest_place() == current_place and user.find_nearest_place() != None:
        print(66666666666666)
        current_place = user.find_nearest_place()
        count_time += 1
        # time.sleep(1)
        context = {
        # 'place': user.place_api
        'place':place_api
        }
        return render(request, template_name="nearby/location.html", context=context)
    elif count_time != 0:
        print(77777777777777)
        user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)
        count_time = 0

    

    if count_time >= 900:  # more than 15 mins #get data from db current place
        try:
            print(88888888888888)
            place_all = Place.objects.values_list('place_name', flat=True)
        except:
            print(99999999999999999)
            place_all = []
        
        # pid = ""  # place id

        if current_place.get('name') in place_all:  # save new place to Place table
            print(100000000000000)
            pid = Place.objects.get(place_name=current_place.get('name')).idplace

        else:
            print("aaaaaaaaaaaaaaaaa")
            Place.objects.create(
                place_name=current_place.get('name'),
                latitude=current_place.get('geometry').get('location').get('lat'),
                longitude=current_place.get('geometry').get('location').get('lng'),
            )
            pid = Place.objects.get(place_name=current_place.get('name')).idplace



        try:
            print("bbbbbbbbbbbbbb")
            place_user = PlaceUser.objects.all().filter(place_idplace=pid, user_iduser=uid)
            count_time_avg = (place_user[0].avg_spending_time * place_user[0].visit_count + place_user[0].avg_spending_time) / (place_user[0].visit_count + 1)
            visited_count = place_user[0].visit_count + 1
            rank_point = compute_rank_point(visited_count, count_time_avg)  # compute rank point

            new_pu = PlaceUser.objects.get(place_idplace=pid,user_iduser=uid)
            new_pu.visit_count=visited_count
            new_pu.avg_spending_time=count_time_avg
            new_pu.save()

        except:
            print("cccccccccccccccccc")
            new_pu = PlaceUser(
                place_idplace=Place.objects.get(idplace=pid),
                user_iduser=User.objects.get(iduser=uid),
                visit_count=1,
                avg_spending_time=count_time,
                ranking= compute_rank_point(1, count_time)
            )
            new_pu.save()





        # count_time_avg = (db.get(current_place).count_time*db.get(
        #     current_place).visited_count+count_time)/(db.get(current_place).visited_count+1)
        # visited_count = db.get(current_place).visited_count+1
        # rank_point = compute_rank_point(
        #     visited_count, count_time_avg)  # compute rank point
        # db.save(current_place, visited_count,
        #         count_time, rank_point)  # save to db

        count_time = 0
        visited_count = 0
        current_place = None
    current_place = user.find_nearest_place()
    context = {
        # 'place': user.place_api
        'place' : user.place_api
    }

    return render(request, template_name="nearby/location.html", context=context)