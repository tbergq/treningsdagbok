from django.conf.urls import include, url
from django.contrib import admin
from account import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'treningsdagbok.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^account/', include('account.urls')),
    url(r'^programs/', include('programs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^workout/', include('workout.urls')),
]
