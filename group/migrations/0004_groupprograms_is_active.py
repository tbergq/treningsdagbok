# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_groupprograms'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupprograms',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
