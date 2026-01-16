import json
from django.shortcuts import render
from weather.models import WeatherRecord
from core.services.climate_service import ClimateService
from core.exceptions.climate import ClimateServiceError


def home(request):
    city = request.GET.get("city")
    weather_data = None
    error_message = None
    history = []
    labels = []
    temperatures = []

    if city:
        service = ClimateService()

        try:
            weather_data = service.get_weather_by_city(city)
            
            # Salvar o registro no banco de dados
            WeatherRecord.objects.create(
                city=weather_data["city"],
                country=weather_data.get("country", ""),
                temperature=weather_data["temperature"],
                feels_like=weather_data["feels_like"],
                humidity=weather_data["humidity"],
                condition=weather_data["condition"],
            )
        except ClimateServiceError as error:
            error_message = str(error)
        
        # Buscar histórico apenas da cidade consultada
        history = WeatherRecord.objects.filter(
            city__iexact=city
        ).order_by('-created_at')[:10]

        if history:
            # Reverter para ordem cronológica para o gráfico
            chart_data = reversed(history)
            labels = [record.created_at.strftime("%d/%m %H:%M") for record in chart_data]
            
            # Recriar chart_data para não consumir o reversed
            chart_data = reversed(history)
            temperatures = [record.temperature for record in chart_data]

    context = {
        "weather": weather_data,
        "error": error_message,
        "history": history,
        "labels": json.dumps(labels),
        "temperatures": json.dumps(temperatures),
    }

    return render(request, "core/home.html", context)






