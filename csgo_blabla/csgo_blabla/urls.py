"""csgo_blabla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve as serve
import player.views as player_view
import csgo_blabla.settings as settings

urlpatterns = [
    url(r'^search/', player_view.playerinfo, name='getPlayerNum'),
    url(r'^player/', player_view.player, name='player'),
    url(r'^admin/', admin.site.urls),
    url( r'^static/(?P<path>.*)$', serve,{ 'document_root': settings.STATIC_URL }),
    url(r'^', player_view.index)
]
