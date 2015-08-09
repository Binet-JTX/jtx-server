import datetime
import re

from django.db import models
from django.utils import timezone, text

from rest_framework import serializers

from jtx_video.models.file import VideoFileSerializer, SubtitleFileSerializer


class Video(models.Model):
    class Meta:
        app_label = "jtx_video"
    
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    date_diffusion = models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))
    views = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    poster = models.ImageField(upload_to='posters/videos', max_length=254, blank=True, null=True)
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
        else:
            if self.pk:
                orig = Video.objects.get(pk=self.pk)
                self.poster = orig.poster

        if add_poster:
            extension = re.sub(r"(.*)\.(?P<ext>[a-zA-Z]+)$", r"\g<ext>", self.poster.name) 
            self.poster.name = text.slugify(self.title) + "." + extension

        super(Video, self).save(*args, **kwargs)


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        read_only_fields = ('views', 'deleted_at', 'deleted', )

    files = VideoFileSerializer(many=True, read_only=True)
    subtitles = SubtitleFileSerializer(read_only=True)


