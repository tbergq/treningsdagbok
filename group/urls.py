# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from group import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='group_index'),
        )