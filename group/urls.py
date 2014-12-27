# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from group import views


urlpatterns = patterns('',
        url(r'^$', views.MyGroups.as_view(), name='group_index'),
        url(r'^purchase_info/$', views.PurchaseInfo.as_view(), name='purchase_info'),
        url(r'^group_info/(?P<group_id>\w+)/$', views.ShowRequestedGroup.as_view(), name='group_info'),
        url(r'^invite/$', views.invite_member, name='invite'),
        )