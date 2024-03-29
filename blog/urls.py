from django.conf.urls import url
from . import views



urlpatterns = [

    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/private$', views.private, name='private'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    
]
