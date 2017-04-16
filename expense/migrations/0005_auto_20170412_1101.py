# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20170412_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_at',
            field=models.DateField(verbose_name='Date', auto_now_add=True),
        ),
    ]
