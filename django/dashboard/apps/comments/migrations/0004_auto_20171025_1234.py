# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20171025_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenters',
            new_name='commenter',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='commenters',
            new_name='commenter',
        ),
    ]
