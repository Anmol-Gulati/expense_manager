# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_expense_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
