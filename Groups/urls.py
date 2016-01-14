from django.conf.urls import url, patterns
from Groups import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^groups/$', views.GroupsList.as_view()),
	url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupsDetail.as_view()),
	url(r'^invite/$', views.InviteList.as_view()),
	url(r'^invite/(?P<pk>[0-9]+)/$', views.InviteDetail.as_view()),
	url(r'^groupMembers/$', views.GroupMembersList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)