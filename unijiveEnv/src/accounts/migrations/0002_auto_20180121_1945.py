# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-21 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(default='/webpages/static/icons_/account_icon.PNG', upload_to=''),
        ),
    ]