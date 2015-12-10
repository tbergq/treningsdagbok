# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Program', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('day_program', models.ForeignKey(to='Program.Day')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExcerciseRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('set_number', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight', models.TextField(max_length=128)),
                ('note', models.TextField(max_length=128, blank=True)),
                ('day_excersice', models.ForeignKey(to='Program.Exercise')),
                ('day_register', models.ForeignKey(to='Workout.DayRegister')),
            ],
        ),
    ]
