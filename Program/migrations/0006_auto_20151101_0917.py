# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '0005_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='user',
            field=models.ForeignKey(to='Account.UserProfile'),
        ),
    ]
