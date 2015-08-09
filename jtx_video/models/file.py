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

    filename = models.CharField(max_length=254)
    extension = models.CharField(max_length=10, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    def level(self):
        lev = 0
        tmp = self.parent
        while tmp:
            lev += 1
            tmp = tmp.parent

        return lev

    def path(self):
        p = self.filename
        tmp = self.parent
        while tmp:
            p = tmp.filename + "/" + p
            tmp = tmp.parent

        return p

    def __str__(self):
        return self.filename


class Folder(BaseFile):
    def nb_elements(self):
        return len(self.basefile_set.all())

    def is_empty(self):
        return self.nb_elements() == 0


class VideoFile(BaseFile):
    bitrate = models.FloatField(blank=True) # in kB/s
    width = models.IntegerField(blank=True) # in px
    height = models.IntegerField(blank=True) # in px
    video = models.ForeignKey(Video, related_name="files", blank=True)


class SubtitleFile(BaseFile):
    video = models.OneToOneField(Video, related_name="subtitles", blank=True)
    