
from django.db import models

class WeatherRecord(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=10)

    temperature = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()

    condition = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C ({self.created_at.date()})"
