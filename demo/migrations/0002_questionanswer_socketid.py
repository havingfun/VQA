# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-11 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='socketid',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Time'),
        ),
    ]
