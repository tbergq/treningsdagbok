# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from programs import views
from programs.views import CreateWeek, AddDayProgram, AddExerciseToDay, ShowDayPartialView

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^new_program/$', views.new_program, name='new_program'),
        url(r'^create_exercise/$', views.create_exercise, name='create_exercise'),
        url(r'^show_excercises/$', views.show_excercises, name='show_excercises'),
        url(r'^add_week/(?P<program_id>\w+)/$', CreateWeek.as_view(),name='add_week'),
        url(r'^add_day/(?P<week_id>\w+)/$', AddDayProgram.as_view(),name='add_day'),
        url(r'^add_exercise_to_day/(?P<day_id>\w+)/$', AddExerciseToDay.as_view(),name='add_exercise_to_day'),
        url(r'^show_day/(?P<day_id>\w+)/$', ShowDayPartialView.as_view(),name='show_day'),
        )

