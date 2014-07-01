from django.conf.urls import patterns, url
from slist import views

urlpatterns = patterns('',
    url(r'^$', views.index.as_view(), name='index')
  )
