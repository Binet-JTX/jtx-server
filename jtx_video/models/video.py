import datetime
import re

from django.db import models
from django.utils import timezone, text
from django.http import Http404

from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response


class Video(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    date_diffusion = models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))
    views = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    poster = models.ImageField(upload_to='posters/videos', max_length=254, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        add_poster = False
        if self.poster:
            if not self.pk:
                add_poster = True
            else:
                orig = Video.objects.get(pk=self.pk)
                if orig.poster != self.poster:
                    orig.poster.delete()
                    add_poster = True

        if add_poster:
            extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", self.poster.name) 
            self.poster.name = text.slugify(self.title) + "." + extension

        super(Video, self).save(*args, **kwargs)


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

    @decorators.detail_route(methods=['put'])
    def remove_poster(self, request, pk=None):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404()

        video.poster.delete()

        serializer = self.get_serializer_class()(video)
        return Response(serializer.data)

