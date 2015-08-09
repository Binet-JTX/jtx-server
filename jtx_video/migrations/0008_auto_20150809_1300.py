# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0007_video_projection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
