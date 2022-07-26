from django.contrib import admin
import django.urls
from .views import home


urlpatterns = [
    django.urls.path('home/', home),

]