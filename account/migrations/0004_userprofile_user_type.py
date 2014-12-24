# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.ForeignKey(default=1, to='account.UserType'),
            preserve_default=True,
        ),
    ]
