# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_events', '0003_auto_20150906_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(null=True, blank=True, upload_to='posters/events'),
        ),
    ]
