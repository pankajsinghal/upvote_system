# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votes', '0004_auto_20150509_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='votes',
        ),
        migrations.AddField(
            model_name='photo',
            name='downvotes',
            field=models.ForeignKey(related_name='downvotes', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='upvotes',
            field=models.ForeignKey(related_name='upvotes', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
