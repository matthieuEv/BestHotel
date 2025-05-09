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
    # Assign a static image to each hotel (hotel1.jpg to hotel10.jpg)
    hotels_with_images = []
    for idx, hotel in enumerate(hotels):
        image_number = (idx % 10) + 1  # Cycle through 1 to 10 for image filenames
        hotel.image_filename = f"bestHotelApp/images/hotel{image_number}.jpg"  # Set image filename attribute
        hotels_with_images.append(hotel)
    return render(request, "bestHotelApp/index.html", {
        "cities": cities,
        "hotels": hotels_with_images,
        "selected_city": selected_city,
    })
