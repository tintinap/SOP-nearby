from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_location(request):
    # Python Program to Get IP Address and Users' Location
    ip = get_ip(request)
    latlng = location()
    lat = request.POST.get('lat')
    lng = request.POST.get('long')
    place_type = request.GET.get('place_type')

    if request.POST.get('lat') is None or request.POST.get('long') is None:
        lat = latlng[0]
        lng = latlng[1]

    print(lat)
    print(lng)
    print(place_type)
    context = {
        'ip': ip,
        'place_type': place_type
    }
    return render(request, template_name='getInfo/location.html', context=context)


def get_ip(request):
    # import socket
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.connect(('google.com', 80))
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("Your Computer IP Address is: " + ip)
    return ip


def location():
    import geocoder
    my_location = geocoder.ip('me')
    print(my_location.latlng)
    lat = str(my_location.latlng[0])
    lng = str(my_location.latlng[1])

    return lat, lng
