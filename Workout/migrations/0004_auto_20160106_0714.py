# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Program', '0001_initial'),
        ('Workout', '0003_auto_20151221_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneRepMax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('weight', models.FloatField()),
                ('base_exercise', models.ForeignKey(to='Program.BaseExercise')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='otheractivity',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
