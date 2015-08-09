import datetime
import re

from django.db import models
from django.utils import timezone, text

from jtx_events.models import Event


class Projection(models.Model):
    title = models.CharField(max_length=254)
    date = models.DateField()
    poster = models.ImageField(upload_to="posters/projections", blank=True, null=True)
    description = models.TextField(blank=True)
    # event = models.ForeignKey(Event, blank=True, null=True)

    def __str__(self):
        return self.title + self.date.strftime(" (%d/%m/%Y)") if self.title == "" else "Projection du" + self.date.strftime(" %d/%m/%Y")

