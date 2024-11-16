from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from Events.models import Event
from Events.serializers import EventSerializer


class EventAPIList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request):
        return render(request, "index.html")

class EventAPICreate(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventAPIUpdate(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventAPIDelete(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class Index(GenericAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    def get(self, request):
        index = EventSerializer(self.get_queryset(), many=True)
        context = {
            "object_list": index.data,
        }
        return render(request, 'index.html', context=context)

# def index(request):
#     return render(request, 'index.html')
