# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('first_name', models.CharField(max_length=254)),
                ('pseudo', models.CharField(blank=True, max_length=100)),
                ('promotion', models.CharField(blank=True, max_length=100)),
                ('poste', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('value', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TagKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='key',
            field=models.ForeignKey(to='jtx_core.TagKey'),
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('key', 'value')]),
        ),
    ]
