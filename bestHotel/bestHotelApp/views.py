from django.shortcuts import render
from .models import City, Hotel

def index(request):
    """
    Render the index page of the bestHotel application.
    """
    cities = City.objects.all()
    hotels = Hotel.objects.all()
    return render(request, "bestHotelApp/index.html", {
        "cities": cities,
        "hotels": hotels,
    })
