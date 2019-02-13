from django.conf.urls import url

from . import views

app_name = 'posteriors'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posteriors/$', views.posteriors, name='posteriors'),
    url(r'^histogram/$', views.histogram, name='histogram'),
    url(r'^get-min-max-param/$', views.get_min_max_param, name='get_min_max_param'),
]
