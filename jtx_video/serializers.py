from rest_framework import serializers

from jtx.utils import VirtualField
from jtx_video.models.file import BaseFile, Folder, VideoFile, SubtitleFile
from jtx_video.models.video import Video
from jtx_video.models.projection import Projection, VideoProjection


class BaseFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseFile

    level = serializers.IntegerField(read_only=True)
    path = serializers.CharField(read_only=True)


class FolderSerializer(BaseFileSerializer):
    class Meta:
        model = Folder

    _type = VirtualField("Folder")
    nb_elements = serializers.IntegerField(read_only=True)
    is_empty = serializers.BooleanField(read_only=True)


class VideoFileSerializer(BaseFileSerializer):
    class Meta:
        model = VideoFile

    _type = VirtualField("VideoFile")


class SubtitleFileSerializer(BaseFileSerializer):
    class Meta:
        model = SubtitleFile

    _type = VirtualField("SubtitleFile")


class ProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projection
        exclude = ('videos', )


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        read_only_fields = ('views', )

    files = VideoFileSerializer(many=True, read_only=True)
    subtitles = SubtitleFileSerializer(read_only=True)
    projections = ProjectionSerializer(many=True, read_only=True)


class DetailedProjectionSerializer(ProjectionSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    def to_representation(self, projection):
        obj = super(DetailedProjectionSerializer, self).to_representation(projection)

        videos_projs = VideoProjection.objects.filter(projection=projection)
        for video in obj["videos"]:
            video_proj = videos_projs.get(video=video["id"])
            video["rank"] = video_proj.rank

        return obj
        
