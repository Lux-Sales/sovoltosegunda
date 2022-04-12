from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from events.serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
