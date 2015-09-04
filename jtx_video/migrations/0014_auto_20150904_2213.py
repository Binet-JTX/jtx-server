# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0013_folder_subtitlefile_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date_diffusion',
            field=models.DateField(default=datetime.datetime(2015, 1, 1, 0, 0)),
        ),
    ]
