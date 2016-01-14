# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(to='Groups.Group')),
                ('invited', models.ForeignKey(related_name='invited', to=settings.AUTH_USER_MODEL)),
                ('inviter', models.ForeignKey(related_name='inviter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
