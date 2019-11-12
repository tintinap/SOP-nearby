from django.shortcuts import render
from django.http import HttpResponse
from nearby.models import Place, User
from nearby.input import Places
from . import place_nearby
import geocoder
import time

import socket


def compute_rank_point(visited_count, count_time_avg):
    rank = visited_count*0.8+count_time_avg*0.2
    return rank


def get_user_location(request):

    # my_location = geocoder.ip('me')
    # print(my_location.latlng)
    # get_user_location.user_lat = float(my_location.latlng[0])
    # get_user_location.user_lon = float(my_location.latlng[1])

    # get_user_location.user_lat = 13.767268
    # get_user_location.user_lon = 100.5336083

    user_lat = request.GET.get('lat')
    user_lon = request.GET.get('longs')

    if user_lat is None or user_lon is None:
        my_location = geocoder.ip('me')
        get_user_location.user_lat = float(my_location.latlng[0])
        get_user_location.user_lon = float(my_location.latlng[1])
    else:
        user_lat = request.GET.get('lat')
        user_lon = request.GET.get('longs')

    print(user_lat)
    print(user_lon)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 80))
    print("Your Computer IP Address is: " + s.getsockname()[0])
    get_user_location.lo = s.getsockname()[0]

    context = {
        'ip': get_user_location.lo
    }
    return render(request, template_name="nearby/location.html", context=context)


def index(request):
    count_time = 0
    count_time_to_get_api = 0

    place_type = "hospital"  # example
    api_key = "AIzaSyBbq0VljhDuyG5TkqguBiL9Wnnq-_BTa1k"

    get_user_location(request)

    # my_location = geocoder.ip('me')
    # print(my_location.latlng)
    # user_lat = str(my_location.latlng[0])
    # user_lon = str(my_location.latlng[1])

    # print(user_lat)
    # print(user_lon)

    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(('google.com', 80))
    # print("Your Computer IP Address is: " + s.getsockname()[0])
    # print(request.GET.get('lat'))
    # print(request.GET.get('long'))

    place_api = place_nearby.places_nearby(get_user_location.user_lat, get_user_location.user_lon, place_type, api_key)
    # print(place_api)

    user = Places(get_user_location.user_lat,get_user_location.user_lon, place_api, get_user_location.lo)
    # user = Places(18.333383,99.3613414, place_api, get_user_location.lo)
    
    try:
        db = User.objects.get(ip=user.ip_id)  # get IP from User db
    except:
        User.objects.create(ip=user.ip_id)  # save to db

    # while service_running():
        # my_location = geocoder.ip('me')
        # print(my_location.latlng)
        # user_lat = str(my_location.latlng[0])
        # user_lon = str(my_location.latlng[1])
        # user.user_lat = user_lat
        # user.user_lon = user_lon
    get_user_location(request)
    user.user_lat = get_user_location.user_lat
    user.user_lon = get_user_location.user_lon

    if user.find_nearest_place() != None:  # in some place #place_view_port() function to find nearest place
        user.places = place_nearby.places_nearby(
            user.user_lat, user.user_lon, place_type, api_key)  # get place location
        user.rank_place
        # send_place_to_output(place_api)???
        print(1111111111111111111111111111111)
        print(user.find_nearest_place())
        current_place = user.find_nearest_place()['name']
        print(current_place)
        print(22222222222222222)
        while user.find_nearest_place()['name'] == current_place:
            get_user_location(request)
            user.user_lat = get_user_location.user_lat
            user.user_lon = get_user_location.user_lon
            count_time += 1
            time.sleep(1)  # not sure function
            user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)  # get new api after get out place
            user.rank_place
            # send_place_to_output(place_api)

        else:  # outside the place
            if count_time_to_get_api == 60:
                get_user_location(request)
                user.user_lat = get_user_location.user_lat
                user.user_lon = get_user_location.user_lon
                user.places = place_nearby.places_nearby(user.user_lat, user.user_lon, place_type, api_key)  # get new api after pass by 1 min
                user.rank_place
                # send_place_to_output(place_api)
                count_time_to_get_api = 0

            else:
                count_time_to_get_api += 1
            time.sleep(1)

        # if count_time >= 900:  # more than 15 mins #get data from db current place
        #     count_time_avg = (db.get(current_place).count_time*db.get(
        #         current_place).visited_count+count_time)/(db.get(current_place).visited_count+1)
        #     visited_count = db.get(current_place).visited_count+1
        #     rank_point = compute_rank_point(
        #         visited_count, count_time_avg)  # compute rank point
        #     db.save(current_place, visited_count,
        #             count_time, rank_point)  # save to db

        count_time = 0
        visited_count = 0
        current_place = ""

    return HttpResponse(place_api)
