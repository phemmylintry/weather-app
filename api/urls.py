from django.urls import path
from .views import home,get_weather

urlpatterns = [
    path('', home, name='get-cord'),
    path('weather', get_weather, name='weather')
]
