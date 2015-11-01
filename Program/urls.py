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
]

urlpatterns = format_suffix_patterns(urlpatterns)