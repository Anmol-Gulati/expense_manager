# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0005_auto_20170412_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.TextField()),
                ('amount', models.IntegerField(default=0)),
                ('created_at', models.DateField(verbose_name='Date', auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='description',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
        migrations.AddField(
            model_name='amount',
            name='category',
            field=models.ForeignKey(to='expense.Expense'),
        ),
        migrations.AddField(
            model_name='amount',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
