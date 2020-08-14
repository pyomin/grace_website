from django.shortcuts import render
from .models import Recommend
from django.views.generic import ListView


class RecommendList(ListView):
    model = Recommend

    def get_queryset(self):
        return Recommend.objects.order_by('-created')


def index(request):
    recommends = Recommend.objects.all()
    return render(
        request,
        'grace/main.html',
        {
            'recommends': recommends,
        }
    )