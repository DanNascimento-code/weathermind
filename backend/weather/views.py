from django.shortcuts import render
from .models import WeatherRecord

def home(request):
    city = request.GET.get("city")

    weather_history = []
    labels = []
    temperatures = []

    if city:
        weather_history = WeatherRecord.objects.filter(
            city__iexact=city
        ).order_by("-created_at")[:10]

        # invertendo para ordem cronológica
        weather_history = reversed(weather_history)

        for record in weather_history:
            labels.append(record.created_at.strftime("%d/%m"))
            temperatures.append(record.temperature)

    context = {
        "city": city,
        "labels": labels,
        "temperatures": temperatures,
    }

    return render(request, "weather/home.html", context)

