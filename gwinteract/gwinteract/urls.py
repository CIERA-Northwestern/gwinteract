"""gwinteract URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.home, name='home'),
    url(r'^posteriors/', include('posteriors.urls'), name='posteriors'),
    url(r'^calculations/', include('calculations.urls'), name='calculations'),
    url(r'^waveforms/', include('waveforms.urls'), name='waveforms'),
    url(r'^newevent/', include('newevent.urls'), name='newevent'),
    url(r'^popsynth/', include('popsynth.urls'), name='popsynth'),
    url(r'^popsynth-generation/', include('popsynth_generation.urls'), name='popsynth_generation'),
    url(r'^admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.STATIC_URL)
