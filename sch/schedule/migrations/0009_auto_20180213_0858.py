# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-13 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_auto_20180212_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(choices=[(b'0', b'-'), (b'1', b'CD'), (b'2', b'CC'), (b'3', b'NP'), (b'4', b'MAP'), (b'5', b'AI'), (b'6', b'EE'), (b'7', b'NA')], max_length=1, primary_key=True, serialize=False),
        ),
    ]