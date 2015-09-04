import re

from django.http import Http404
from django.db.models import Prefetch

from rest_framework import viewsets, decorators
from rest_framework.response import Response

from jtx_video.models.file import BaseFile, SubtitleFile, VideoFile
from jtx_video.models.video import Video
from jtx_video.models.projection import Projection, VideoProjection
from jtx_video.serializers import VideoSerializer, ProjectionSerializer, DetailedProjectionSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.prefetch_related(
        Prefetch('files', queryset=VideoFile.objects.all()),
        Prefetch('subtitles', queryset=SubtitleFile.objects.all()),
        Prefetch('projections', queryset=Projection.objects.all())
    )
    serializer_class = VideoSerializer
    filter_fields = {
        'date_diffusion': ['lte', 'gte'],
    }
    search_fields = ('title', 'description')

    @decorators.detail_route(methods=['put'])
    def remove_poster(self, request, pk=None):
        try:
            video = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404()

        video.poster.delete()

        serializer = self.get_serializer_class()(video)
        return Response(serializer.data)


class ProjectionViewSet(viewsets.ModelViewSet):
    queryset = Projection.objects.all()
    serializer_class = ProjectionSerializer
    filter_fields = ('date', )
    search_fields = ('title', )

    def retrieve(self, request, pk=None, *args, **kwargs):
        qs = Projection.objects.prefetch_related(
            Prefetch('videos', queryset=Video.objects.prefetch_related(
                Prefetch('files', queryset=VideoFile.objects.all()),
                Prefetch('subtitles', queryset=SubtitleFile.objects.all()),
                Prefetch('projections', queryset=Projection.objects.all()),
                Prefetch('video_projections', queryset=VideoProjection.objects.filter(projection=pk)),
            )),
        )
        instance = qs.get(pk=pk)

        serializer = DetailedProjectionSerializer(instance, context={'video_projections': instance.video_projections})
        return Response(serializer.data)


