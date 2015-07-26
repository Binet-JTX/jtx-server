import datetime

from django.db import models
from django.utils import timezone
from django.http import Http404

from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response


class Event(models.Model):
    """
    An event covered by the JTX, or during which have taken place one or more projections
    """
    title = models.CharField(max_length=254)
    description = models.TextField()
    begin_date = models.DateTimeField(default=datetime.datetime(2015, 1, 1))
    end_date = models.DateTimeField(default=datetime.datetime(2015, 1, 1))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        read_only_fields = ('deleted_at', 'deleted', )

    def validate(self, data):
        if data['begin_date'] > data['end_date']:
            raise serializers.ValidationError("end date must occur after begin date")
        return data


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_fields = {
        'begin_date': ['lte', 'gte'],
        'end_date': ['lte', 'gte'],
    }
    search_fields = ('title', 'description')

    @decorators.detail_route(methods=['put'])
    def cancel(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404()

        event.deleted = True
        event.deleted_at = timezone.now()
        event.save()

        serializer = self.get_serializer_class()(event)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404()

        event.deleted = False
        event.deleted_at = None
        event.save()

        serializer = self.get_serializer_class()(event)
        return Response(serializer.data)