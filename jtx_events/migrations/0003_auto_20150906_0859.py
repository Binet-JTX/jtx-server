# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_events', '0002_auto_20150809_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='begin_date',
            field=models.DateField(default=datetime.datetime(2015, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 1, 1, 0, 0)),
        ),
    ]
