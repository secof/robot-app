# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsettings',
            name='selenium_hub_ip',
            field=models.GenericIPAddressField(null=True, protocol='IPv4'),
        ),
    ]