# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0010_auto_20150809_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='video',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='video',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='video',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='projection',
            name='videos',
            field=models.ManyToManyField(related_name='projections', to='jtx_video.Video', through='jtx_video.VideoProjection'),
        ),
    ]
