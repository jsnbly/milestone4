from django.urls import path, include
from django.conf.urls import url
from .views import create_contact, contact_detail

urlpatterns = [
    #url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', contact_detail, name='contact_detail'),
    url(r'^new/$', create_contact, name='contact'),
    #url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]