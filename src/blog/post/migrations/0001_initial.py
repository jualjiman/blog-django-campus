# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
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
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'posts')),
                ('post_body', models.TextField()),
                ('start_date', models.DateTimeField(default=datetime.datetime(2015, 8, 31, 15, 46, 46, 606838), help_text='Fecha y hora en que aparecera la publicaci\xf3n.')),
                ('end_date', models.DateTimeField(help_text='Fecha y hora en que dejar\xe1 de ser mostrado la publicaci\xf3n.', null=True, blank=True)),
                ('repository_link', models.URLField(help_text='Enlace del repositorio.', blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='Esta publicaci\xf3n esta activa?.')),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(help_text=b'A que categoria pertenece la publicaci\xc3\xb3n?.', to='post.Category')),
            ],
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Texto descriptivo del archivo.', max_length=100)),
                ('attachment', models.FileField(help_text=b'Archivo de publicaci\xc3\xb3n', upload_to=b'post_file')),
                ('post', models.ForeignKey(to='post.Post')),
            ],
            options={
                'verbose_name': 'Archivo de publicaci\xf3n',
                'verbose_name_plural': 'Archivos de publicaci\xf3n',
            },
        ),
        migrations.CreateModel(
            name='PostReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Texto descriptivo del enlace.', max_length=100)),
                ('link', models.URLField(help_text='Enlace de apoyo de la publicaci\xf3n.')),
                ('post', models.ForeignKey(to='post.Post')),
            ],
            options={
                'verbose_name': 'Post Reference',
                'verbose_name_plural': 'Post References',
            },
        ),
        migrations.CreateModel(
            name='PostVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Texto descriptivo del video.', max_length=100)),
                ('youtube_video_code', models.CharField(help_text='Codigo de video de youtube', max_length=20)),
                ('post', models.ForeignKey(to='post.Post')),
            ],
            options={
                'verbose_name': 'Post Videos',
                'verbose_name_plural': 'Post Videos',
            },
        ),
    ]
