# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataDictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.EmailField(max_length=100)),
                ('notes', models.TextField(blank=True, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'verbose_name_plural': 'data dictionaries',
            },
        ),
        migrations.CreateModel(
            name='DataDictionaryField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('dataType', models.CharField(choices=[(b'NUMBER', b'Number'), (b'TEXT', b'Text'), (b'LONGTEXT', b'Longtext'), (b'DATE', b'Date'), (b'TIME', b'Time'), (b'DATETIME', b'Datetime')], default=b'TEXT', max_length=10)),
                ('parent_dict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datafreezer.DataDictionary')),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=250)),
                ('date_uploaded', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('uploaded_by', models.EmailField(max_length=254)),
                ('date_begin', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('vertical_slug', models.CharField(max_length=25)),
                ('hub_slug', models.CharField(max_length=25)),
                ('dataset_file', models.FileField(upload_to=b'datafreezer/uploads/%Y/%m/%d/')),
                ('attachments', models.FileField(blank=True, null=True, upload_to=b'')),
                ('could_parse', models.NullBooleanField()),
                ('appears_in', models.ManyToManyField(blank=True, to='datafreezer.Article')),
                ('data_dictionary', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='datafreezer.DataDictionary')),
            ],
        ),
    ]