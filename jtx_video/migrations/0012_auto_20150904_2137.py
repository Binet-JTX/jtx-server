# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0011_auto_20150809_1423'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='basefile',
        #     name='parent',
        # ),
        # migrations.RemoveField(
        #     model_name='folder',
        #     name='basefile_ptr',
        # ),
        # migrations.RemoveField(
        #     model_name='subtitlefile',
        #     name='basefile_ptr',
        # ),
        # migrations.RemoveField(
        #     model_name='subtitlefile',
        #     name='video',
        # ),
        # migrations.RemoveField(
        #     model_name='videofile',
        #     name='basefile_ptr',
        # ),
        # migrations.RemoveField(
        #     model_name='videofile',
        #     name='video',
        # ),
        migrations.DeleteModel(
            name='Folder',
        ),
        migrations.DeleteModel(
            name='SubtitleFile',
        ),
        migrations.DeleteModel(
            name='VideoFile',
        ),
        migrations.DeleteModel(
            name='BaseFile',
        ),
    ]
