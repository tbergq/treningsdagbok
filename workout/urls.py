# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from workout import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^select/(?P<pk>\w+)/$', views.LoadExercise.as_view(), name="select"),
        url(r'^register/(?P<day_id>\w+)/$', views.RegisterWorkout.as_view(), name="register"),
        url(r'^register_partial/(?P<day_id>\w+)/(?P<exercise_id>\w+)/$', views.RegisterPartial.as_view(), name="register_partial"),
        )
