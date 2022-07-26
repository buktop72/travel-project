from django.shortcuts import render

def home(requests):
    context = {"name": "Stepan"}
    return render(requests, "home.html", context)
