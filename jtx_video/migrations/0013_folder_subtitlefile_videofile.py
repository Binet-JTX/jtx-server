# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0012_auto_20150904_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('filename', models.CharField(default='foo', max_length=254)),
                ('extension', models.CharField(max_length=10, blank=True)),
                ('parent', models.ForeignKey(null=True, to='jtx_video.Folder', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubtitleFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('filename', models.CharField(default='foo', max_length=254)),
                ('extension', models.CharField(max_length=10, blank=True)),
                ('parent', models.ForeignKey(null=True, to='jtx_video.SubtitleFile', blank=True)),
                ('video', models.OneToOneField(related_name='subtitles', to='jtx_video.Video', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('filename', models.CharField(default='foo', max_length=254)),
                ('extension', models.CharField(max_length=10, blank=True)),
                ('bitrate', models.FloatField(blank=True)),
                ('width', models.IntegerField(blank=True)),
                ('height', models.IntegerField(blank=True)),
                ('parent', models.ForeignKey(null=True, to='jtx_video.VideoFile', blank=True)),
                ('video', models.ForeignKey(related_name='files', to='jtx_video.Video', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
