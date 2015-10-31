# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('muscle_group', models.CharField(max_length=128, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('youtube_link', models.CharField(max_length=128, blank=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='baseexercise',
            unique_together=set([('name', 'muscle_group')]),
        ),
    ]
