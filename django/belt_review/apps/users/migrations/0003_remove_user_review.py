# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 03:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='review',
        ),
    ]
