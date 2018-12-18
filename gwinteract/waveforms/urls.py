from django.conf.urls import url

from . import views

app_name = 'waveforms'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^waveforms/$', views.waveforms, name='waveforms'),
    url(r'^plot/$', views.plot, name='plot'),
]
