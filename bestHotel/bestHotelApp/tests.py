from django.test import TestCase, Client
from .models import City, Hotel
from django.urls import reverse
from django.core.management import call_command
from io import StringIO
from unittest.mock import patch

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

class ImportCSVCommandTests(TestCase):
    # I've used chatGPT to help me better understand how Mock works
    # and how to use it in the context of Django tests.
    # I also used StackOverflow and the Python documentation
    
    def setUp(self):
        self.city_csv = 'AMS;Amsterdam\nANT;Antwerp\n'
        self.hotel_csv = 'AMS;AMS01;Hotel Amsterdam\nANT;ANT01;Hotel Antwerp\n'

    @patch('requests.get')
    def test_import_csv_command(self, mock_get):
        class MockResponse:
            def __init__(self, text):
                self.text = text
            def raise_for_status(self):
                pass
        # Simulate two calls: first for city.csv, then for hotel.csv
        mock_get.side_effect = [MockResponse(self.city_csv), MockResponse(self.hotel_csv)]
        out = StringIO()
        call_command('import_csv', stdout=out)
        self.assertTrue(City.objects.filter(code='AMS', name='Amsterdam').exists())
        self.assertTrue(Hotel.objects.filter(code='AMS01', name='Hotel Amsterdam').exists())
        self.assertIn('Import completed.', out.getvalue())
