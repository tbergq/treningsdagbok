from django.conf.urls import patterns, url
from account import views

urlpatterns = patterns('',
        url(r'^$', views.login, name='index'),
        url(r'^login/', views.login, name='login'),
        url(r'^logout/', views.logout, name='logout'),
        url(r'^create_user/', views.create_user, name='create_user'),
        url(r'^create_group/', views.CreateGroupForm.as_view(), name='create_group'),
        )

