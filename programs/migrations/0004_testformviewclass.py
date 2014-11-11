# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20141025_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestFormViewClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('alder', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
