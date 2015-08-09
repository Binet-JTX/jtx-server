# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0009_auto_20150809_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoProjection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.PositiveSmallIntegerField()),
                ('projection', models.ForeignKey(to='jtx_video.Projection')),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='projection',
        ),
        migrations.AddField(
            model_name='videoprojection',
            name='video',
            field=models.ForeignKey(to='jtx_video.Video'),
        ),
        migrations.AddField(
            model_name='projection',
            name='videos',
            field=models.ManyToManyField(to='jtx_video.Video', through='jtx_video.VideoProjection'),
        ),
    ]
