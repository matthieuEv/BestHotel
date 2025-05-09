from django.apps import AppConfig


class BesthotelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bestHotelApp'

    def ready(self):

        def fetch_and_import_csv():
            import csv
            import requests
            from .models import City, Hotel

            CITY_CSV_URL = "http://rebecca.maykinmedia.nl/djangocase/city.csv"
            HOTEL_CSV_URL = "http://rebecca.maykinmedia.nl/djangocase/hotel.csv"

            # Import city.csv
            try:
                resp = requests.get(CITY_CSV_URL)
                resp.raise_for_status()
                lines = resp.text.splitlines()
                reader = csv.reader(lines, delimiter=';')
                for i, row in enumerate(reader):
                    if len(row) != 2:
                        continue
                    code = row[0]
                    name = row[1]
                    City.objects.update_or_create(
                        code=code,
                        defaults={"name": name}
                    )
            except Exception as e:
                print(f"Error importing city.csv: {e}")

            # Import hotel.csv
            try:
                resp = requests.get(HOTEL_CSV_URL)
                resp.raise_for_status()
                lines = resp.text.splitlines()
                reader = csv.reader(lines, delimiter=';')
                for i, row in enumerate(reader):
                    if len(row) != 3:
                        continue
                    city_code = row[0]
                    code = row[1]
                    name = row[2]
                    city = City.objects.filter(code=city_code).first()
                    if city:
                        Hotel.objects.update_or_create(
                            code=code,
                            defaults={
                                "name": name,
                                "city": city
                            }
                        )
            except Exception as e:
                print(f"Error importing hotel.csv: {e}")

        fetch_and_import_csv()
