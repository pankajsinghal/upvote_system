# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votes', '0009_auto_20150509_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='downvotes',
        ),
        migrations.AddField(
            model_name='photo',
            name='downvotes',
            field=models.ManyToManyField(related_name='downvotes', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
