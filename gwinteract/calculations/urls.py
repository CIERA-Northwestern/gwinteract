from django.conf.urls import url

from . import views

app_name = 'calculations'
urlpatterns = [
    url(r'^$', views.calculations, name='calculations'),
]
