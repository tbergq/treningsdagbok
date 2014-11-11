# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from workout import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^select/(?P<program_id>\w+)/$', views.LoadExercise.as_view(), name="select"),
        )
