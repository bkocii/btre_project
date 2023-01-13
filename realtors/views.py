from django.shortcuts import render

from .models import Realtor

def realtors(request):
    realtors = Realtor.objects.all()

    context = {
        'realtors': realtors
    }

    return render(request, '/pages/about.html', context)
