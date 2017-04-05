# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount',
            name='expense',
        ),
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Amount',
        ),
    ]
