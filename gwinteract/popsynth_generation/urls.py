from django.conf.urls import url

from . import views

app_name = 'popsynth_generation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^population-synthesis-form/$', views.population_synthesis_form, name='population_synthesis_form'),
]
