from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.authtoken import views
from Account.views import UserView, UserListView, UserInfoView, ChangePassword, PasswordReset

urlpatterns = patterns('',
    url(r'^auth/', views.obtain_auth_token),
    url(r'^userInfo/', UserInfoView.as_view()),
    url(r'^users/', UserListView.as_view()),
    url(r'^changePassword/', ChangePassword.as_view()),
    url(r'^resetPassword/', PasswordReset.as_view()),
)