# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 15, 54, 31, 983451), help_text='Fecha y hora en que aparecera la publicaci\xf3n.'),
        ),
    ]
