PROJECT_PATH := "bestHotel"
MANAGE := python $(PROJECT_PATH)/manage.py

run:
	$(MANAGE) runserver

migrate:
	$(MANAGE) makemigrations bestHotelApp
	$(MANAGE) migrate
