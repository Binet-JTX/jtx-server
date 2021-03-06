import datetime
import re

from django.db import models
from django.utils import timezone, text

from jtx_events.models import Event
from jtx_video.models.video import Video


class Projection(models.Model):
    title = models.CharField(max_length=254)
    date = models.DateField()
    description = models.TextField(blank=True)
    videos = models.ManyToManyField(Video, through='VideoProjection', related_name='projections')
    event = models.ForeignKey(Event, related_name='projections')
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title + self.date.strftime(" (%d/%m/%Y)") if self.title != "" else "Projection du" + self.date.strftime(" %d/%m/%Y")


class VideoProjection(models.Model):
    video = models.ForeignKey(Video, related_name='video_projections')
    projection = models.ForeignKey(Projection, related_name='video_projections')
    rank = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.projection.__str__() + " (" + "{0:0>3}".format(self.rank) + ") " + self.video.__str__()

