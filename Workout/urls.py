from django.conf.urls import url, patterns
from Workout import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	#url(r'^baseExercises/$', views.BaseExerciseList.as_view()),
	#url(r'^baseExercises/(?P<pk>[0-9]+)/$', views.BaseExerciseDetail.as_view()),
	url(r'^registerDay/list/(?P<day_id>[0-9]+)/$', views.RegisterDayList.as_view()),
	url(r'^registerDay/(?P<pk>[0-9]+)/$', views.RegisterDayDetail.as_view()),
	url(r'^exerciseRegister/$', views.ExcerciseRegisterList.as_view()),
	url(r'^lastRegistered/$', views.GetLastRegisteredList.as_view()),
	url(r'^exerciseRegisterForUser/$', views.RegisterDayAllForUserList.as_view()),
	
]

urlpatterns = format_suffix_patterns(urlpatterns)