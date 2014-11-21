# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile'),
        ('programs', '0002_auto_20141121_2114'),
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('day_program', models.ForeignKey(to='programs.DayProgram')),
                ('user', models.ForeignKey(to='account.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExcerciseRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('set_number', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight', models.TextField(max_length=128)),
                ('note', models.TextField(max_length=128, blank=True)),
                ('day_excersice', models.ForeignKey(to='programs.DayExcersice')),
                ('day_register', models.ForeignKey(to='workout.DayRegister')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
