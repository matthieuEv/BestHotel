import csv
import requests
import os
from django.core.management.base import BaseCommand
from bestHotelApp.models import Hotel, City

class Command(BaseCommand):
    help = 'Import hotel and city data from remote CSV files.'

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str, help='URL of the CSV file to import')
        parser.add_argument('--username', type=str, help='Username for HTTP authentication')
        parser.add_argument('--password', type=str, help='Password for HTTP authentication')

    def handle(self, *args, **options):
        # URLs and credentials for the exercise
        CITY_CSV_URL = "http://rebecca.maykinmedia.nl/djangocase/city.csv"
        HOTEL_CSV_URL = "http://rebecca.maykinmedia.nl/djangocase/hotel.csv"
        USERNAME = os.environ.get("BEST_HOTEL_USERNAME")
        PASSWORD = os.environ.get("BEST_HOTEL_PASSWORD")
        if not USERNAME:
            USERNAME = input("HTTP username for the CSV: ")
        if not PASSWORD:
            import getpass
            PASSWORD = getpass.getpass("HTTP password for the CSV: ")

        # Import city.csv
        try:
            resp = requests.get(CITY_CSV_URL, auth=(USERNAME, PASSWORD))
            resp.raise_for_status()
            lines = resp.text.splitlines()
            reader = csv.reader(lines, delimiter=';')
            for row in reader:
                if len(row) != 2:
                    continue
                code, name = row
                City.objects.update_or_create(
                    code=code,
                    defaults={"name": name}
                )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing city.csv: {e}'))
            return

        # Import hotel.csv
        try:
            resp = requests.get(HOTEL_CSV_URL, auth=(USERNAME, PASSWORD))
            resp.raise_for_status()
            lines = resp.text.splitlines()
            reader = csv.reader(lines, delimiter=';')
            for row in reader:
                if len(row) != 3:
                    continue
                city_code, code, name = row
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
            self.stderr.write(self.style.ERROR(f'Error importing hotel.csv: {e}'))
            return

        self.stdout.write(self.style.SUCCESS('Import completed.'))
