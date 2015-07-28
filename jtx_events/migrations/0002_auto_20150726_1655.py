# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='begin_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc)),
        ),
    ]
