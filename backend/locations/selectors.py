from .models import Location

def get_default_location():
    return Location.objects.first()

     