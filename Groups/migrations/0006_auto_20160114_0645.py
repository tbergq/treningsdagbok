# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0005_auto_20160114_0640'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='groupmembers',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='invite',
            unique_together=set([]),
        ),
    ]
