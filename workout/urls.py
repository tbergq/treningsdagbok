# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from workout import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^select/(?P<pk>\w+)/$', views.LoadExercise.as_view(), name="select"),
        url(r'^register/(?P<day_id>\w+)/(?P<program_id>\w+)/$', views.RegisterWorkout.as_view(), name="register"),
        url(r'^register_partial/(?P<day_id>\w+)/(?P<exercise_id>\w+)/$', views.RegisterPartial.as_view(), name="register_partial"),
        url(r'^start_register/(?P<id>\w+)/(?P<program_id>\w+)/$', views.StartDayRegister.as_view(), name="start_register"),
        url(r'^get_previous_register_data/(?P<exercise_id>\w+)/$', views.get_previous_register_data, name="get_previous_register_data"),
        url(r'^finish_registering/(?P<program_id>\w+)/$', views.finish_register, name="finish_register"),
        url(r'^registered_workouts/$', views.ShowRegisteredExercises.as_view(), name='registered_workouts'),
        )
