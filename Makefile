PROJECT_PATH := "bestHotel"
MANAGE := python $(PROJECT_PATH)/manage.py

serve:
	$(MANAGE) runserver 

migrate:
	$(MANAGE) makemigrations bestHotelApp
	$(MANAGE) migrate

setup_admin:
	$(MANAGE) createsuperuser

run:
	$(MANAGE) flush --noinput
	$(MAKE) migrate
	$(MAKE) setup_admin
	$(MAKE) serve

test:
	$(MANAGE) test bestHotelApp

flush:
	$(MANAGE) flush --noinput
