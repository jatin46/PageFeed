# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-23 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20170407_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]