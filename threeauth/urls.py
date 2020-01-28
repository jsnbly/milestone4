from django.conf.urls import url, include
from . import url_reset
from .views import index, registration, user_profile, logout, login

urlpatterns = [
    url(r'^register/$', registration, name='registration'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
]