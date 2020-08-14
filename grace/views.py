from django.shortcuts import render
from .models import Recommend

# Create your views here.


def index(request):
    recommends = Recommend.objects.all()
    return render(
        request,
        'grace/main.html',
        {
            'recommends': recommends,
        }
    )