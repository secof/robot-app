# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AppSettings(models.Model):
    git_repo = models.CharField(max_length=150, blank=True)
    selenium_hub_ip = models.GenericIPAddressField(protocol='IPv4', null=True)
    selenium_hub_port = models.PositiveIntegerField(blank=True)
    selenium_os = models.CharField(max_length=150, blank=True)
    selenium_browser = models.CharField(max_length=150, blank=True)
    tests_folder_path = models.CharField(max_length=150, blank=True)


