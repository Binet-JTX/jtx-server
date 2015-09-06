# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0014_auto_20150904_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projection',
            name='poster',
        ),
        migrations.AddField(
            model_name='projection',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='videoprojection',
            name='projection',
            field=models.ForeignKey(related_name='video_projections', to='jtx_video.Projection'),
        ),
        migrations.AlterField(
            model_name='videoprojection',
            name='video',
            field=models.ForeignKey(related_name='video_projections', to='jtx_video.Video'),
        ),
    ]
