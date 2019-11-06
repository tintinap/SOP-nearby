from django.shortcuts import render
from django.http import HttpResponse
from nearby.models import Place, User
from nearby.input import Places

def index(request):
    place = Place.objects.values_list('place_name')
    user = Places(1, 2, 112)  # get user_locate,place_api,ip_id
    db = User.objects.values_list('ip')  # get IP from User db
    if user.ip_id not in db:  # check db
        User.objects.create(ip=user.ip_id) # save to db


    # if 'op' not in place:
    #     return HttpResponse("STP")

    return HttpResponse(place)

def main():
    count_time = 0
    count_time_to_get_api = 0

        # db.save(user.ip_id)  # save from db
#
#     while service_running():
#         user.user_location = get_user_location()  # get user ip???
#
#         if user.find_nearest_place != None:  # in some place #place_view_port() function to find nearest place
#             user.places = from_google_api(location=current_user_location, radius=5000)  # get place location
#             user.rank_place
#             # send_place_to_output(place_api)???
#             current_place = user.find_nearest_place
#
#             while user.find_nearest_place != None:
#                 user.user_location = get_user_location()
#                 count_time += 1
#                 time.sleep(1)  # not sure function
#
#         else:  # outside the place
#             if count_time_to_get_api == 60:
#                 user.places = from_google_api(location=current_user_location,
#                                               radius=5000)  # get new api after pass by 1 min
#                 user.rank_place
#                 # send_place_to_output(place_api)
#                 count_time_to_get_api = 0
#
#             else:
#                 count_time_to_get_api += 1
#             time.sleep(1)
#
#         places = from_google_api(location=current_user_location, radius=5000)  # get new api after get out place
#         user.rank_place
#         # send_place_to_output(place_api)
#
#         if count_time >= 900:  # more than 15 mins #get data from db current place
#             count_time_avg = (db.get(current_place).count_time * db.get(current_place).visited_count + count_time) / (
#                         db.get(current_place).visited_count + 1)
#             visited_count = db.get(current_place).visited_count + 1
#             rank_point = compute_rank_point(visited_count, count_time_avg)  # compute rank point
#             db.save(current_place, visited_count, count_time, rank_point)  # save to db
#
#         count_time = 0
#         visited_count = 0
#         current_place = ""
#
#
# def compute_rank_point(visited_count, count_time_avg):  # thinking...
#
