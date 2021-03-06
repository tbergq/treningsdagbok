# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from group import views


urlpatterns = patterns('',
        url(r'^$', views.MyGroups.as_view(), name='group_index'),
        url(r'^purchase_info/$', views.PurchaseInfo.as_view(), name='purchase_info'),
        url(r'^group_info/(?P<group_id>\w+)/$', views.ShowRequestedGroup.as_view(), name='group_info'),
        url(r'^invite/$', views.invite_member, name='invite'),
        url(r'^show_programs_to_add/$', views.ShowProgramsAvailableForGroupAdd.as_view(), name='show_programs_to_add'),
        url(r'^add_program/$', views.AddProgramToGroup.as_view(), name='add_program'),
        url(r'^user_workout_info/(?P<user_id>\w+)/(?P<group_id>\w+)/$', views.ShowGroupUserWorkouts.as_view(), name='user_workout_info'),
        )