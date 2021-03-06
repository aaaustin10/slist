from django.conf.urls import patterns, url
from slist import views

urlpatterns = patterns('',
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^lists$', views.lists.as_view(), name='lists'),
    url(r'^lists/(?P<list_id>\d+)$', views.items.as_view(), name='list'),
  )
