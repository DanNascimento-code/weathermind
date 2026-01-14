from .models import Location

def create_location(*, city, country, region=None, latitude=None, longitude=None):
    location = Location.objects.create(
        city=city,
        country=country,
        region=region or "",
        latitude=latitude,
        longitude=longitude,
    )
    return location
 
  