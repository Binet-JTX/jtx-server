import datetime
import re

from django.db import models
from django.utils import timezone, text
from django.http import Http404

from rest_framework import serializers, viewsets, decorators
from rest_framework.response import Response

from jtx_video.models.video import Video


class BaseFile(models.Model):
    class Meta:
        app_label = "jtx_video"
        abstract = True

    filename = models.CharField(max_length=254)
    extension = models.CharField(max_length=10, blank=True)
    parent = models.ForeignKey('self', blank=True)

    def level(self):
        if not self.parent:
            return 0
        else:
            return 1 + level(self.parent)

    def path(self):
        if not self.parent:
            return "/"
        else:
            return path(self.parent) + filename

    def __str__(self):
        return self.filename


class Folder(BaseFile):
    pass
    def nb_elements(self):
        return len(self.children_set)

    def id_empty(self):
        return self.nb_elements(self) == 0


class VideoFile(BaseFile):
    bitrate = models.FloatField(blank=True) # in kB/s
    width = models.IntegerField(blank=True) # in px
    height = models.IntegerField(blank=True) # in px
    video = models.ForeignKey(Video, related_name="files", blank=True)


class SubtitleFile(BaseFile):
    video = models.OneToOneField(Video, related_name="subtitles", blank=True)
    