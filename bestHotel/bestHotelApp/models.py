from django.db import models

class City(models.Model):
    code = models.CharField(
        max_length=10,
        primary_key=True,
        help_text="Unique city code"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.code} ({self.name})"


class Hotel(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    city = models.ForeignKey(
        City,
        db_column='city_code',
        on_delete=models.CASCADE,
        related_name='hotels'
    )

    def __str__(self):
        return f"{self.name} ({self.city.code})"

