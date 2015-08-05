import datetime

from django.db import models
from django.utils import timezone
from django.http import Http404

from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response


class Video(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    date_diffusion = models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))
    views = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        read_only_fields = ('views', 'deleted_at', 'deleted', )


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_fields = {
        'date_diffusion': ['lte', 'gte'],
    }
    search_fields = ('title', 'description')

    @decorators.detail_route(methods=['put'])
    def remove(self, request, pk=None):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404()

        video.deleted = True
        video.deleted_at = timezone.now()
        video.save()

        serializer = self.get_serializer_class()(video)
        return Response(serializer.data)

    @decorators.detail_route(methods=['put'])
    def restore(self, request, pk=None):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404()

        video.deleted = False
        video.deleted_at = None
        video.save()

        serializer = self.get_serializer_class()(video)
        return Response(serializer.data)

