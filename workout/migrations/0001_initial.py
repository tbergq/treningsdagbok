# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0005_delete_testformviewclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateField()),
                ('day_program', models.ForeignKey(to='programs.DayProgram')),
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
