# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0017_video_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtitlefile',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, to='jtx_video.Folder'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, to='jtx_video.Folder'),
        ),
    ]
