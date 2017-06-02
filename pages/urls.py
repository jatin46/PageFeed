from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^(?P<page_id>[0-9]+)/$', views.pageDetail, name='pagedetail'),
    url(r'^create/$', views.create, name='create_check'),
	url(r'^comment/(?P<post_id>[0-9]+)/$', views.comment, name='comments'),
]