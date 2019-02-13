from django.conf.urls import url

from . import views

app_name = 'newevent'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newevent/$', views.newevent, name='newevent'),
]
