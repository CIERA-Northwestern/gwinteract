from django.conf.urls import url

from . import views

app_name = 'popsynth'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popsynth/$', views.popsynth, name='popsynth'),
    url(r'^plot_bns/$', views.plot_bns, name='plot_bns'),
]
