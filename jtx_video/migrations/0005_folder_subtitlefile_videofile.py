# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0004_auto_20150805_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('filename', models.CharField(max_length=254)),
                ('extension', models.CharField(max_length=10, blank=True)),
                ('parent', models.ForeignKey(blank=True, to='jtx_video.Folder')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubtitleFile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('filename', models.CharField(max_length=254)),
                ('extension', models.CharField(max_length=10, blank=True)),
                ('parent', models.ForeignKey(blank=True, to='jtx_video.SubtitleFile')),
                ('video', models.OneToOneField(to='jtx_video.Video', blank=True, related_name='subtitles')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('filename', models.CharField(max_length=254)),
                ('extension', models.CharField(max_length=10, blank=True)),
                ('bitrate', models.FloatField(blank=True)),
                ('width', models.IntegerField(blank=True)),
                ('height', models.IntegerField(blank=True)),
                ('parent', models.ForeignKey(blank=True, to='jtx_video.VideoFile')),
                ('video', models.ForeignKey(to='jtx_video.Video', blank=True, related_name='files')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
