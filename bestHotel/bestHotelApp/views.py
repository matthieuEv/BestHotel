from django.shortcuts import render
from .models import City, Hotel

def index(request):
    """
    Render the index page of the bestHotel application.
    """
    cities = City.objects.all()
    selected_city = request.GET.get("city", "all")
    if selected_city == "all":
        hotels = Hotel.objects.all()
    else:
        hotels = Hotel.objects.filter(city__code=selected_city)
    return render(request, "bestHotelApp/index.html", {
        "cities": cities,
        "hotels": hotels,
        "selected_city": selected_city,
    })
