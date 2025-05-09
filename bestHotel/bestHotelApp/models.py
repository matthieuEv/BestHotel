from django.db import models

class City(models.Model):
    code = models.CharField(
        max_length=10,
        primary_key=True,
        help_text="Unique city code"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.code} ({self.name})"  # Display city code and name

class Hotel(models.Model):
    code = models.CharField(max_length=20, unique=True)  # Unique hotel code
    name = models.CharField(max_length=255)  # Hotel name
    city = models.ForeignKey(
        City,
        db_column='city_code',
        on_delete=models.CASCADE,
        related_name='hotels'
    )  # Foreign key to City, using city_code as DB column

    def __str__(self):
        return f"{self.name} ({self.city.code})"  # Display hotel name and city code

