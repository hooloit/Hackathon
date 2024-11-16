from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Events.views import EventsAPIViewset

router = routers.SimpleRouter()
router.register(r'Event', EventsAPIViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Events.urls", namespace = 'events')),
    path('reg/', include("Register.urls", namespace = 'register')),
    path('api/v1/', include(router.urls)),
]
