from django.conf.urls import url, patterns
from Workout import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^otherActivity/$', views.OtherActivityList.as_view()),
	url(r'^otherActivity/(?P<pk>[0-9]+)/$', views.OtherActivityDetail.as_view()),
	url(r'^registerDay/list/(?P<day_id>[0-9]+)/$', views.RegisterDayList.as_view()),
	url(r'^registerDay/(?P<pk>[0-9]+)/$', views.RegisterDayDetail.as_view()),
	url(r'^exerciseRegister/$', views.ExcerciseRegisterList.as_view()),
	url(r'^exerciseRegister/(?P<pk>[0-9]+)/$', views.ExcerciseRegisterDetail.as_view()),
	url(r'^lastRegistered/$', views.GetLastRegisteredList.as_view()),
	url(r'^exerciseRegisterForUser/$', views.RegisterDayAllForUserList.as_view()),
	url(r'^exerciseRegisterForDay/(?P<day_register_id>[0-9]+)/$', views.ExcerciseRegisterForDayRegister.as_view()),
	url(r'^dayregister/(?P<program_id>[0-9]+)/$', views.DayRegisterOfProgram.as_view()),
	url(r'^1rm/$', views.OneRepMaxList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)