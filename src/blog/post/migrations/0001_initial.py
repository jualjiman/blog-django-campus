# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Nombre de la categoria', max_length=100)),
                ('is_active', models.BooleanField(default=True, help_text='Esta categoria esta activa?.')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Titulo de la publicaci\xf3n.', max_length=150)),
                ('post_body', models.TextField()),
                ('start_date', models.DateTimeField(default=datetime.datetime(2015, 8, 31, 5, 49, 18, 270338), help_text='Fecha y hora en que aparecera la publicaci\xf3n.')),
                ('end_date', models.DateTimeField(help_text='Fecha y hora en que dejar\xe1 de ser mostrado la publicaci\xf3n.', null=True, blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='Esta publicaci\xf3n esta activa?.')),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(help_text=b'A que categoria pertenece la publicaci\xc3\xb3n?', to='post.Category')),
            ],
        ),
    ]
