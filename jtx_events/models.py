import datetime

from django.db import models
from django.utils import timezone

from rest_framework import serializers


class Event(models.Model):
    """
    An event covered by the JTX, or during which have taken place one or more projections
    """
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    begin_date = models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))
    end_date = models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))

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



