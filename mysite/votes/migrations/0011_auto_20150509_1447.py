# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0010_auto_20150509_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='downvotes',
            field=models.ManyToManyField(related_name='downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='upvotes',
            field=models.ManyToManyField(related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
