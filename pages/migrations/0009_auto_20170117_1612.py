# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-17 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_check1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpage',
            name='cover_page',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]