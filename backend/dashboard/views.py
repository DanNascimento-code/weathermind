from django.shortcuts import render
from locations.selectors import get_default_location

def index(request):
    location = get_default_location()

    context = {
        "location": location,
    }

    return render(request, "dashboard/index.html", context)

