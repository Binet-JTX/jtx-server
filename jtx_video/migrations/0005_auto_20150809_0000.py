# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0004_auto_20150805_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('filename', models.CharField(max_length=254)),
                ('extension', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('basefile_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='jtx_video.BaseFile')),
            ],
            bases=('jtx_video.basefile',),
        ),
        migrations.CreateModel(
            name='SubtitleFile',
            fields=[
                ('basefile_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='jtx_video.BaseFile')),
                ('video', models.OneToOneField(blank=True, to='jtx_video.Video', related_name='subtitles')),
            ],
            bases=('jtx_video.basefile',),
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('basefile_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='jtx_video.BaseFile')),
                ('bitrate', models.FloatField(blank=True)),
                ('width', models.IntegerField(blank=True)),
                ('height', models.IntegerField(blank=True)),
                ('video', models.ForeignKey(blank=True, to='jtx_video.Video', related_name='files')),
            ],
            bases=('jtx_video.basefile',),
        ),
        migrations.AddField(
            model_name='basefile',
            name='parent',
            field=models.ForeignKey(blank=True, to='jtx_video.BaseFile', null=True),
        ),
    ]
