# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_testformviewclass'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestFormViewClass',
        ),
    ]
