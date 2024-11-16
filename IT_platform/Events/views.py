from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Events.models import Event
from Events.serializers import EventSerializer


# Viewset для таблицы Event
class EventsAPIViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class Index(GenericAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    def get(self, request):
        return render(request, 'index.html')

# def index(request):
#     return render(request, 'index.html')
