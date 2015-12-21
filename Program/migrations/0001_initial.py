# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('youtube_link', models.CharField(max_length=128, blank=True)),
                ('description', models.CharField(max_length=128, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('set', models.CharField(max_length=10)),
                ('reps', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128, null=True, blank=True)),
                ('break_time', models.TextField(max_length=10, blank=True)),
                ('base_exercise', models.ForeignKey(related_name='base_exercises', to='Program.BaseExercise')),
                ('day', models.ForeignKey(related_name='exercises', to='Program.Day')),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(related_name='program', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('program', models.ForeignKey(related_name='weeks', to='Program.Program')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='week',
            field=models.ForeignKey(related_name='days', to='Program.Week'),
        ),
        migrations.AddField(
            model_name='baseexercise',
            name='muscle_group',
            field=models.ForeignKey(related_name='muscle_group', to='Program.MuscleGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='baseexercise',
            unique_together=set([('name', 'muscle_group')]),
        ),
    ]
