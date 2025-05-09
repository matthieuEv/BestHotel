PROJECT_PATH := "bestHotel"
MANAGE := python $(PROJECT_PATH)/manage.py

serve:
	$(MANAGE) runserver

migrate:
	$(MANAGE) makemigrations bestHotelApp
	$(MANAGE) migrate

setup_admin:
	$(MANAGE) createsuperuser --username admin --email a@e.com

run:
	$(MANAGE) flush --noinput
	$(MAKE) migrate
	$(MAKE) setup_admin
	$(MAKE) serve
