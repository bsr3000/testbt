# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170308_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='/home/andrey/PycharmProjects/testbt/media/default.jpg', null=True, upload_to='/home/andrey/PycharmProjects/testbt/media/user_photos/'),
        ),
    ]
