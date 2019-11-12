from django.shortcuts import render
from django.http import HttpResponse
from nearby.models import Place, User, PlaceUser
from nearby.input import Places


def index(request):
    place = Place.objects.values_list('place_name')
    user = Places(1, 2, 1223)  # get user_location,place_api,ip_id
    # if user.ip_id not in User.objects.values_list('ip', flat=True):  # check db
    #     User.objects.create(ip=user.ip_id)  # save to db

    count_time = 0
    count_time_to_get_api = 0

    get_ip = User.objects.get(ip=user.ip_id)
    uid = get_ip.iduser  # user id

    # TEST VALUE #########
    current_place = [{'geometry': {'location': {'lat': 12.56, 'lng': 24.56}},
                      'name': 'faaaa', }]

    place_all = Place.objects.values_list('place_name', flat=True)
    pid = ""  # place id

    if current_place[0].get('name') in place_all:  # save new place to Place table
        pid = Place.objects.get(place_name=current_place[0].get('name')).idplace

    else:
        Place.objects.create(
            place_name=current_place[0].get('name'),
            latitude=current_place[0].get('geometry').get('location').get('lat'),
            longitude=current_place[0].get('geometry').get('location').get('lng'),
        )
        pid = Place.objects.get(place_name=current_place[0].get('name')).idplace
    # rank_place(pid)
    while True:

        ### ยังใช้ไม่ได้ vvvvv ###########################################################################

        # if user.find_nearest_place != None:  # in some place #place_view_port() function to find nearest place
        #     user.places = from_google_api(location=current_user_location, radius=5000)  # get place location
        #     user.rank_place # send_place_to_output(place_api)???
        #
        #     #######################################
        #     current_place = user.find_nearest_place
        #     #######################################
        #
        #     while user.find_nearest_place != None:
        #         user.user_location = get_user_location()
        #         count_time += 1
        #         time.sleep(1)  # not sure
        #
        # else:  # outside the place
        #     if count_time_to_get_api == 60:
        #         user.places = from_google_api(location=current_user_location, radius=5000)  # get new api after 1 min
        #         user.rank_place
        #         # send_place_to_output(place_api)
        #         count_time_to_get_api = 0
        #
        #     else:
        #         count_time_to_get_api += 1
        #
        #     time.sleep(1)
        #
        # places = from_google_api(location=current_user_location, radius=5000)  # get new api after out of place
        # user.rank_place
        # send_place_to_output(place_api)

        #############################################################################################

        count_time += 1
        if count_time >= 900:  # > 15 minutes #get data from current place dict

            # (test) place_user = PlaceUser.objects.all().filter(place_idplace=1, user_iduser=1)

            # match user's and place's id
            try:
                place_user = PlaceUser.objects.all().filter(place_idplace=pid, user_iduser=uid)
                count_time_avg = (place_user[0].avg_spending_time * place_user[0].visit_count +
                                  place_user[0].avg_spending_time) / (place_user[0].visit_count + 1)
                visited_count = place_user[0].visit_count + 1
                # rank_point = compute_rank_point(visited_count, count_time_avg)  # compute rank point

                new_pu = PlaceUser.objects.get(place_idplace=pid,user_iduser=uid)
                new_pu.visit_count=visited_count
                new_pu.avg_spending_time=count_time_avg
                new_pu.save()

                # return HttpResponse('OK')

            except:
                new_pu = PlaceUser(
                    place_idplace=Place.objects.get(idplace=pid),
                    user_iduser=User.objects.get(iduser=uid),
                    visit_count=1,
                    avg_spending_time=count_time,
                    ranking=1
                )
                new_pu.save()

                # return HttpResponse("this value is not in table")

    # all_place = []
    # all_user = PlaceUser.objects.all().filter(user_iduser=uid)
    # for i in all_user:
    #     all_place.append(i.place_idplace)

    # return HttpResponse(all_place[0].idplace) -> return = Id list in Place table