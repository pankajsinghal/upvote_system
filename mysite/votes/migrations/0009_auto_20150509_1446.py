# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votes', '0008_auto_20150509_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.AddField(
            model_name='photo',
            name='downvotes',
            field=models.ForeignKey(related_name='downvotes', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.RemoveField(
            model_name='photo',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='photo',
            name='upvotes',
            field=models.ManyToManyField(related_name='upvotes', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
