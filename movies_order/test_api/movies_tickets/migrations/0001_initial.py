# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cinema_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('price', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'cinemas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('movie_name', models.CharField(max_length=20)),
                ('ellipsis', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=20)),
                ('vision', models.CharField(max_length=10, blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_base',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('movie_name', models.CharField(max_length=20)),
                ('ellipsis', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=20)),
                ('vision', models.CharField(max_length=10, blank=True, null=True)),
                ('duration', models.CharField(max_length=3)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=20, blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_detail',
                'managed': False,
            },
        ),
    ]
