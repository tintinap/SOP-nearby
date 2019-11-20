import time
import googlemaps

def main():
    print(1)
    print(places_nearby("13.8754862","100.3751903","hospital","AIzaSyBbq0VljhDuyG5TkqguBiL9Wnnq-_BTa1k"))

def places_nearby(lat, lng, place_type, api_key, language='en'):
    """
    lat, lng  : String - Latitide and Longitude
    place_type : String - same as type tag in google map api(places api)
    language : String - same as language agrument in google map api(places api)
    api_key : String - your api key from google
    
    return list of places that will contain name, geometry and types of places api's result
    """

    API_KEY = api_key
    location = str(lat)+","+str(lng)
    gmaps = googlemaps.Client(API_KEY)
    places_result0 = []
    places_result1 = []
    places_result2 = []
    places_result0 = gmaps.places_nearby(
        location = location,
        radius = 5000,
        type = place_type,
        language = language,
    )
    # print(places_result0)
    if 'next_page_token' in places_result0:
        time.sleep(3)
        places_result1 = gmaps.places_nearby(page_token= places_result0['next_page_token'])
        if 'next_page_token' in places_result1:
            time.sleep(3)
            places_result2 = gmaps.places_nearby(page_token= places_result1['next_page_token'])

    p0, p1,  p2 = [], [], []
    place_r = [places_result0, places_result1, places_result2]
    p_r = [p0, p1, p2]
    #geometry, name, types
    for j in range(len(place_r)):
        if 'results' in place_r[j]:
            for i in range(len(place_r[j]['results'])):
                place_temp = {'name' : [],'geometry' : [],'types' : []}
                place_temp['geometry'] = place_r[j]['results'][i]['geometry']
                place_temp['name'] = place_r[j]['results'][i]['name']
                place_temp['types'] = place_r[j]['results'][i]['types']
                p_r[j].append(place_temp)
    places_result = p0 + p1 +p2
    # print(len(places_result))
    return places_result

main()