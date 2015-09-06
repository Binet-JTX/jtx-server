# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0016_projection_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
