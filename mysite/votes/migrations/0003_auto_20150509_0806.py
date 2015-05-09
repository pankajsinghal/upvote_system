# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_auto_20150509_0759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='image',
        ),
    ]
