from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from weather.services.openweather import fetch_weather
from weather.services.history import get_city_history
import json

def home(request):
    city = request.GET.get("city")

    context = {}

    if city:
        weather = fetch_weather(city)
        history = get_city_history(city)

        context["weather"] = weather
        context["history"] = history
        
        # Preparar dados para o gráfico
        if history:
            labels = [record.created_at.strftime("%d/%m %H:%M") for record in history]
            temperatures = [record.temperature for record in history]
            context["labels"] = json.dumps(labels, cls=DjangoJSONEncoder)
            context["temperatures"] = json.dumps(temperatures, cls=DjangoJSONEncoder)

    return render(request, "core/home.html", context)


    