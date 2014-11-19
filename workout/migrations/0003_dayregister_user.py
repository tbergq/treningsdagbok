# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userprofile_user_type'),
        ('workout', '0002_auto_20141112_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='dayregister',
            name='user',
            field=models.ForeignKey(default=1, to='account.UserProfile'),
            preserve_default=False,
        ),
    ]
