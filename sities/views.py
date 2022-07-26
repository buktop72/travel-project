from django.shortcuts import render
from .models import City


def home(requests):
    qs = City.objects.all()
    context = {'cities': qs}
    return render(requests, "cities/home.html", context)
