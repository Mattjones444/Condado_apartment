from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.

def index(request):
    """ A view to return the index page """

    google_api_key = settings.GOOGLE_MAPS_API

    context = {
        'google_api_key': os.getenv('GOOGLE_MAPS_API')
    }

    return render(request, 'home/index.html', context)
