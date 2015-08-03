# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('begin_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('end_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0, tzinfo=utc))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
