from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.video_list, name='list'),
    url(r'^(?P<video_id>\d+)/$', views.video_detail, name='detail'),
    url(r'^new$', views.video_new, name='new'),
    url(r'^(?P<video_id>\d+)/delete$', views.video_delete, name='delete'),
]
