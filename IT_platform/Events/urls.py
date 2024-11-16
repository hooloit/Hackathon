from django.urls import path
from .views import *

app_name = "event"

urlpatterns = [
    path('', index, name="index"),
]
