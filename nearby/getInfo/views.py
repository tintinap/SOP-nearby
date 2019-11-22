from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def get_location(request):
    # Python Program to Get IP Address and Users' Location
    ip = get_ip(request)
    latlng = location(request)
    lat = request.POST.get('lat')
    lng = request.POST.get('long')

    if request.POST.get('lat') is None or request.POST.get('long') is None or request.POST.get('lat') == "" or\
            request.POST.get('long') == "":
        lat = latlng[0]
        lng = latlng[1]

    print(lat)
    print(lng)
    context = {
        'ip': ip,
        'place_type': place_type
    }
    return render(request, template_name='getInfo/location.html', context=context)


place_type = ""


def search(request):
    global place_type
    if request.POST.get('place_type') is not None:
        place_type = request.POST.get('place_type')
    print(place_type)
    context = {
        'place_type': place_type,
    }
    return render(request, template_name='getInfo/search.html', context=context)


def get_ip(request):
    import socket
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(('google.com', 80))
    # ip = s.getsockname()[0]
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("Your Computer IP Address is: " + ip)
    return ip


def location(request):
    import geocoder
    my_location = geocoder.ip('me')  # str(get_ip(request))
    print(my_location.latlng)
    lat = str(my_location.latlng[0])
    lng = str(my_location.latlng[1])

    return lat, lng
