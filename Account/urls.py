from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken import views

urlpatterns = patterns('',
    url(r'^auth/', views.obtain_auth_token),
)