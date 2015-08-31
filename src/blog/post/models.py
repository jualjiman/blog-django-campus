# *-* coding:utf-8 -*-
from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(
        max_length=100,
        help_text=u'Nombre de la categoria'
    )
    is_active = models.BooleanField(
        default=True,
        help_text=u'Esta categoria esta activa?.'
    )


class Post(models.Model):
    title = models.CharField(
        max_length=150,
        help_text=u'Titulo de la publicación.'
    )
    post_body = models.TextField()
    start_date = models.DateTimeField(
        default=datetime.now(),
        help_text=u'Fecha y hora en que aparecera la publicación.',
    )
    end_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text=u'Fecha y hora en que dejará de ser mostrado la publicación.'
    )
    is_active = models.BooleanField(
        default=True,
        help_text=u'Esta publicación esta activa?.'
    )
    category = models.ForeignKey(
        Category,
        help_text="A que categoria pertenece la publicación?"
    )
    author = models.ForeignKey(
        User,
        editable=False
    )
    slug = models.SlugField(
        editable=False,
        unique=True
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
