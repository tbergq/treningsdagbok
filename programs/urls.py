# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from programs import views
from programs.views import ProgramWeeks, AddDayProgram, AddExerciseToDay, ShowDayPartialView, AddDays, AddWeek

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^new_program/$', views.new_program, name='new_program'),
        url(r'^create_exercise/$', views.create_exercise, name='create_exercise'),
        url(r'^show_excercises/$', views.show_excercises, name='show_excercises'),
        url(r'^program_week/(?P<program_id>\w+)/$', ProgramWeeks.as_view(),name='program_week'),
        url(r'^add_day/(?P<week_id>\w+)/$', AddDayProgram.as_view(),name='add_day'),
        url(r'^add_exercise_to_day/(?P<day_id>\w+)/$', AddExerciseToDay.as_view(),name='add_exercise_to_day'),
        url(r'^show_day/(?P<day_id>\w+)/$', ShowDayPartialView.as_view(),name='show_day'),
        url(r'^add_days/$', AddDays.as_view(),name='add_days'),
        url(r'^get_muscle_groups/$', views.get_muscle_groups,name='get_muscle_groups'),
        url(r'^add_week/$', AddWeek.as_view(),name='addweek'),
        url(r'^add_one_day/(?P<week_id>\w+)/$', views.add_day,name='add_one_day'),
        url(r'^delete_confirmation/(?P<day_id>\w+)/$', views.DeleteDayProgram.as_view(),name='delete_confirmation'),
        url(r'^delete_day_program/(?P<day_id>\w+)/$', views.DeleteDayProgramRedirect.as_view(),name='delete_day_program'),
        url(r'^delete_week_confirmaiton/(?P<week_id>\w+)/$', views.DeleteWeekConfirmation.as_view(),name='delete_week_confirmation'),
        url(r'^delete_week/(?P<week_id>\w+)/$', views.DeleteWeek.as_view(),name='delete_week'),
        url(r'^copy_week/(?P<week_id>\w+)/$', views.CopyWeek.as_view(),name='copy_week'),
        url(r'^delete_day_exercise_confirmation/(?P<pk>\w+)/$', views.DeleteDayExercise.as_view(),name='delete_day_exercise'),
        url(r'^exercise_partial/$', views.AddExerciseFormPartial.as_view(), name='exercise_partial'),
        url(r'^get_base_exercises/$', views.get_base_exercises, name='get_base_exercises'),
        url(r'^save_exercises_to_day/(?P<program_id>\w+)/(?P<day_id>\w+)/$', views.save_exercises_to_day, name='save_exercises_to_day'),
        url(r'^edit_day/(?P<pk>\w+)/$', views.EditExerciseView.as_view(), name='edit_day'),
        url(r'^delete_program/(?P<pk>\w+)/$', views.DeleteProgramView.as_view(), name='delete_program'),
        
        )

