# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_auto_20141124_2125'),
        ('group', '0002_auto_20141226_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPrograms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(to='group.Group')),
                ('program', models.ForeignKey(to='programs.Program')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
