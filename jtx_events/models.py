import datetime

from django.db import models

from rest_framework import serializers, viewsets


class Event(models.Model):
    """
    An event covered by the JTX, or during which have taken place one or more projections
    """
    class Meta:
        app_label = 'jtx_event'
    title = models.CharField(max_length=254)
    description = models.TextField()
    begin_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = {
        'begin_date': ['lte', 'gte'],
        'end_date': ['lte', 'gte'],
    }
    search_fields = ('title', 'description')