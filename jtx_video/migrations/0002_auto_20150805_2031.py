# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='date',
            new_name='date_diffusion',
        ),
        migrations.RemoveField(
            model_name='video',
            name='videostatus',
        ),
        migrations.AddField(
            model_name='video',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='VideoStatus',
        ),
    ]
