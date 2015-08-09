# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='event',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='event',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_at',
        ),
    ]
