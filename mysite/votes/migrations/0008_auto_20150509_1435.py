# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_auto_20150509_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='upvotes',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
