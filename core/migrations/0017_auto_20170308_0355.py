# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20170308_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='user_photos/default.jpg', upload_to='user_photos/'),
        ),
    ]
