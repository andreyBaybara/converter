from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include, path


urlpatterns = [
    url(r'^$', views.converter, name='converter'),
    url(r'^convert$', views.convert_value, name='convert_value')
]
