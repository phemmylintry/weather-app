from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
# Create your views here.


def home(request):


    return render(request, 'api/home.html')


def get_weather(request):

    #check if request is ajax or Post
    if request.is_ajax() and request.method != 'POST':
        return JsonResponse({'status' : 'Fail'}, status=400)
    
    #store data in variable text
    lat = request.POST.get('lat', None)
    lon = request.POST.get('long', None)

    URL = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}'.format(lat, lon)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"}
    
    r = requests.get(URL, headers=headers)

    json = r.json()

    details = json['properties']['meta']
    
    return JsonResponse(details, status=200, safe=False)