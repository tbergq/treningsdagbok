from django.conf.urls import url, patterns
from Program import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^baseExercises/$', views.BaseExerciseList.as_view()),
	url(r'^baseExercises/(?P<pk>[0-9]+)/$', views.BaseExerciseDetail.as_view()),
	url(r'^muscleGroups/(?P<pk>[0-9]+)/$', views.MuscleGroupDetail.as_view()),
	url(r'^muscleGroups/$', views.MuscleGroupList.as_view()),
	url(r'^programs/(?P<pk>[0-9]+)/$', views.ProgramDetail.as_view()),
	url(r'^programs/$', views.ProgramList.as_view()),
	url(r'^weeks/$', views.WeekGroupList.as_view()),
	url(r'^weeks/(?P<pk>[0-9]+)/$', views.WeekDetail.as_view()),
	url(r'^days/$', views.DayGroupList.as_view()),
	url(r'^days/(?P<pk>[0-9]+)/$', views.DayDetail.as_view()),
	url(r'^exercises/(?P<pk>[0-9]+)/$', views.ExerciseDetail.as_view()),
	url(r'^exercises/$', views.ExerciseGroupList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)