# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0006_auto_20150809_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='projection',
            field=models.ForeignKey(blank=True, to='jtx_video.Projection', null=True),
        ),
    ]
