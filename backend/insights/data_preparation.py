
def prepare_weather_features(weather_records):
    return {
        "avg_temperature": sum(r.temperature for r in weather_records) / len(weather_records),
        "avg_humidity": sum(r.humidity for r in weather_records) / len(weather_records),
        "conditions": [r.condition for r in weather_records],
        "temperature_trend": weather_records[0].temperature - weather_records[-1].temperature
    }
