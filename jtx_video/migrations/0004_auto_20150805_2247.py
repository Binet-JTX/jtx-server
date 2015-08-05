# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0003_video_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='poster',
            field=models.ImageField(blank=True, null=True, max_length=254, upload_to='posters/videos'),
        ),
    ]
