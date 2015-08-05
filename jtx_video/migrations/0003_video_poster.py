# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0002_auto_20150805_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='poster',
            field=models.ImageField(blank=True, upload_to='posters/videos', max_length=254),
        ),
    ]
