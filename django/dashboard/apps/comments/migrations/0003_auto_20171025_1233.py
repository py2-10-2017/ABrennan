# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-25 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('comments', '0002_auto_20171025_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commenters',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='commentfroms', to='users.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='commenters',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='messagefroms', to='users.User'),
            preserve_default=False,
        ),
    ]
