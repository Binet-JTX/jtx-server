import re

from django.http import Http404

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from jtx_video.models.video import Video, VideoSerializer


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

