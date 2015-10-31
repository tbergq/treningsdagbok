from django.conf.urls import url
from Program import views

urlpatterns = [
	url(r'^baseExercises/$', views.BaseExerciseList.as_view()),
]