# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 01:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_user_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',)},
        ),
    ]
