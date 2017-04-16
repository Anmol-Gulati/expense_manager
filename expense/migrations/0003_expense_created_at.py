# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20170405_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='created_at',
            field=models.DateField(default=datetime.date.today, verbose_name='Day'),
        ),
    ]
