from rest_framework import serializers

from jtx.utils import VirtualField
from jtx_video.models.file import BaseFile, Folder, VideoFile, SubtitleFile
from jtx_video.models.video import Video
from jtx_video.models.projection import Projection


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


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        read_only_fields = ('views', 'deleted_at', 'deleted', )

    files = VideoFileSerializer(many=True, read_only=True)
    subtitles = SubtitleFileSerializer(read_only=True)


class ProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projection


class DetailedProjectionSerializer(ProjectionSerializer):
    videos = VideoSerializer(many=True, read_only=True)
