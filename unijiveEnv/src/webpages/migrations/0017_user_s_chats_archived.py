# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-12 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0016_auto_20180202_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_s_chats',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
