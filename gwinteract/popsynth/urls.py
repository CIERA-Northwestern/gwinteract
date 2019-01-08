from django.conf.urls import url

from . import views

app_name = 'popsynth'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^popsynth/$', views.popsynth, name='popsynth'),
    url(r'^plot_bns/$', views.plot_bns, name='plot_bns'),
    url(r'^plot_nsbh/$', views.plot_nsbh, name='plot_nsbh'),
    url(r'^plot_bbh/$', views.plot_bbh, name='plot_bbh'),
]
