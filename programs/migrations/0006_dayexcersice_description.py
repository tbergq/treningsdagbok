# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_delete_testformviewclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayexcersice',
            name='description',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
