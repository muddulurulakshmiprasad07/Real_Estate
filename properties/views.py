from django.shortcuts import render
from .models import Property

def home(request):

    properties = Property.objects.all()

    context = {
        'properties': properties
    }

    return render(request, 'index.html', context)