# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0008_auto_20150809_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='projection',
            field=models.ForeignKey(to='jtx_video.Projection', blank=True, null=True, related_name='videos'),
        ),
    ]
