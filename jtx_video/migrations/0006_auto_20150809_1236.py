# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jtx_video', '0005_auto_20150809_0000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=254)),
                ('date', models.DateField()),
                ('poster', models.ImageField(upload_to='posters/projections', blank=True, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
