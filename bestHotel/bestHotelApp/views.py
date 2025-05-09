from django.shortcuts import render
from .models import City, Hotel

def index(request):
    """
    Render the index page of the bestHotel application.
    """
    cities = City.objects.all()  # Get all cities for the dropdown
    selected_city = request.GET.get("city", "all")  # Get selected city from GET params, default to 'all'
    if selected_city == "all":
        hotels = Hotel.objects.all()  # Show all hotels if 'all' is selected
    else:
        hotels = Hotel.objects.filter(city__code=selected_city)  # Filter hotels by selected city
    # Assign a stable image to each hotel according to its code
    hotels_with_images = []
    for hotel in hotels:
        image_number = (abs(hash(hotel.code)) % 10) + 1  # Always the same for a given code
        hotel.image_filename = f"bestHotelApp/images/hotel{image_number}.jpg"  # Set image filename attribute
        hotels_with_images.append(hotel)
    return render(request, "bestHotelApp/index.html", {
        "cities": cities,
        "hotels": hotels_with_images,
        "selected_city": selected_city,
    })
