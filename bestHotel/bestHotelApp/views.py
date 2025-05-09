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
    # Assign a static image to each hotel (hotel1.jpg to hotel10.jpg)
    hotels_with_images = []
    for idx, hotel in enumerate(hotels):
        image_number = (idx % 10) + 1
        hotel.image_filename = f"bestHotelApp/images/hotel{image_number}.jpg"
        hotels_with_images.append(hotel)
    return render(request, "bestHotelApp/index.html", {
        "cities": cities,
        "hotels": hotels_with_images,
        "selected_city": selected_city,
    })
