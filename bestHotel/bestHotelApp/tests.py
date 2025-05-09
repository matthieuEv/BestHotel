from django.test import TestCase, Client
from .models import City, Hotel
from django.urls import reverse

class CityHotelModelTests(TestCase):
    def setUp(self):
        self.city = City.objects.create(code="AMS", name="Amsterdam")
        self.hotel = Hotel.objects.create(code="AMS01", name="Hotel Amsterdam", city=self.city)

    def test_city_str(self):
        self.assertIn("AMS", str(self.city))
        self.assertIn("Amsterdam", str(self.city))

    def test_hotel_str(self):
        self.assertIn("Hotel Amsterdam", str(self.hotel))
        self.assertIn("AMS", str(self.hotel))

    def test_hotel_city_relation(self):
        self.assertEqual(self.hotel.city, self.city)

class IndexViewTests(TestCase):
    def setUp(self):
        self.city1 = City.objects.create(code="AMS", name="Amsterdam")
        self.city2 = City.objects.create(code="ANT", name="Antwerp")
        Hotel.objects.create(code="AMS01", name="Hotel Amsterdam", city=self.city1)
        Hotel.objects.create(code="ANT01", name="Hotel Antwerp", city=self.city2)
        self.client = Client()

    def test_index_shows_all_hotels(self):
        response = self.client.get(reverse("bestHotelApp:index"))
        self.assertContains(response, "Hotel Amsterdam")
        self.assertContains(response, "Hotel Antwerp")

    def test_index_filter_by_city(self):
        response = self.client.get(reverse("bestHotelApp:index"), {"city": "AMS"})
        self.assertContains(response, "Hotel Amsterdam")
        self.assertNotContains(response, "Hotel Antwerp")
