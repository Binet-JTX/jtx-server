# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('begin_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0))),
                ('end_date', models.DateTimeField(default=datetime.datetime(2015, 1, 1, 0, 0))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
