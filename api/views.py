from django.shortcuts import render
import requests
import json
# Create your views here.


def home(request):


    return render(request, 'api/home.html')


def get_weather(request):

    """
    Retruns JSON response containing sorted list.
    Gets request from Post method or ajax, passes request into quick_sort function, 
    returns JSONResponse of sorted list
    """

    #check if request is ajax or Post
    if request.is_ajax() and request.method != 'POST':
        
        return JsonResponse({'status' : 'Fail'}, status=400)
    
    #store data in variable text
    lat = request.POST.get('lat', None)
    lon = request.POST.get('long', None)

    URL = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={}&lon={}'.format(lat, lon)
    print(URL)
    r = requests.get(URL)

    result = json.loads(r.content.decode('utf-8'))

    print(result)