# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 01:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_review'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.User'),
            preserve_default=False,
        ),
    ]
