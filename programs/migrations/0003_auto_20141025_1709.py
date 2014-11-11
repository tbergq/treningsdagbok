# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_userprofile_user_type'),
        ('programs', '0002_auto_20141025_1544'),
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
