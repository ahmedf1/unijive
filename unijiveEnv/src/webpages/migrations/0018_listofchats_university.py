# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-16 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0017_user_s_chats_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofchats',
            name='university',
            field=models.CharField(default='NYU', max_length=45),
            preserve_default=False,
        ),
    ]