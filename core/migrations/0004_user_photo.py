# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 02:18
from __future__ import unicode_literals

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170307_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='/home/andrey/PycharmProjects/testbt/media/user_photos/'),
        ),
    ]
