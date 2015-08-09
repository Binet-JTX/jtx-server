from rest_framework import viewsets, decorators
from rest_framework.response import Response

from jtx_events.models import Event, EventSerializer

# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = {
        'begin_date': ['lte', 'gte'],
        'end_date': ['lte', 'gte'],
    }
    search_fields = ('title', 'description')