# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_events', '0003_auto_20150906_0859'),
        ('jtx_video', '0015_auto_20150906_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='projection',
            name='event',
            field=models.ForeignKey(related_name='projections', to='jtx_events.Event', default=2),
            preserve_default=False,
        ),
    ]
