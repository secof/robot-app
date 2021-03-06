# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git_repo', models.CharField(blank=True, max_length=150)),
                ('selenium_hub_ip', models.GenericIPAddressField(protocol='IPv4')),
                ('selenium_hub_port', models.PositiveIntegerField(blank=True)),
                ('selenium_os', models.CharField(blank=True, max_length=150)),
                ('selenium_browser', models.CharField(blank=True, max_length=150)),
                ('tests_folder_path', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
