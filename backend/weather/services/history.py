
from weather.models import WeatherRecord

def get_city_history(city, limit=7):
    return WeatherRecord.objects.filter(
        city__iexact=city
    ).order_by("-created_at")[:limit]
