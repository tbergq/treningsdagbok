# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile'),
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('muscle_group', models.CharField(max_length=128, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('user', models.ForeignKey(to='account.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DayExcersice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('set', models.CharField(max_length=10)),
                ('reps', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=128, null=True)),
                ('base_excersice', models.ForeignKey(to='programs.BaseExercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DayProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(to='account.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('program', models.ForeignKey(to='programs.Program')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dayprogram',
            name='week',
            field=models.ForeignKey(to='programs.Week'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dayexcersice',
            name='day_program',
            field=models.ForeignKey(to='programs.DayProgram'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='baseexercise',
            unique_together=set([('name', 'user')]),
        ),
    ]
