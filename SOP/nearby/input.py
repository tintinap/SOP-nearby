import math


class Places:

    def __init__(self, user_location, place_api, ip_id):
        self.user_location = user_location  # lat/lng of user
        self.places = place_api  # list of place for checking where are the nearby place that user can enter
        self.ip_id = ip_id  # IP is a username of user
        self.place_api = []  # array for sorted place
#
#     def r_user_to_place(self, user_lat, user_lon, place_lat,
#                         place_lon):  # need edit to match with places api and user location that get
#         dlat = math.radians(place_lat - user_lat)  # should be self.user.lat self.place.lat
#         dlon = math.radians(place_lon - user_lon)
#         a = math.pow(math.sin(dlat / 2), 2) + math.cos(math.radians(place_lat)) * math.cos(
#             math.radians(user_lat)) * math.pow(math.sin(dlon / 2), 2)
#         c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#         d = 6373 * c
#         d = round(d, 3)
#         return d
#
#     def find_nearest_place(self):  # need edit to match with places api that get
#         nearest_place = None
#         r = 0
#         for i in self.places:
#             if self.r_user_to_place(self.user_location.lat, self.user_location.lon, self.places[i].lat,
#                                     self.places[i].lon) < self.r_user_to_place(self.places[i].viewport.lat1,
#                                                                                self.places[i].viewport.lon1,
#                                                                                self.places[i].viewport.lat2,
#                                                                                self.places[i].viewport.lon2) / 2
#                 if r >= self.r_user_to_place(self.user_location.lat, self.user_location.lon, self.places[i].lat,
#                                              self.places[i].lon) and r != 0:
#                     nearest_place = self.places[i]
#         return nearest_place  # save r to this var too
#
#     def rank_place(self):  # can upgrad performance by check with tag #need edit to match with places api that get
#         place_saved = []
#         place_unsaved = []
#         for i in self.places:
#             if self.places[i] in db.getall(place):
#                 place_saved.append(self.places[i])
#             else:
#                 place_unsaved.append(self.places[i])
#         self.place_api = place_saved.sort + place_unsaved.sort  # place_saved sort by rank in db #place_unsaved sort by distance

# test
# acc = Place(1,2,3)
# acc.r_user_to_place(38.898556,-77.037852,38.897147,-77.043934)

# print(acc.r_user_to_place(38.898556,-77.037852,38.897147,-77.043934))