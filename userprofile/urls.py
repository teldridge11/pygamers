from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from models import Game
import views

urlpatterns = [
    url(r'^$', views.user_profile, name='userprofile'),
    url(r'^addGame/$', views.add_game, name='addGame'),
    url(r'^editGame/(?P<id>\d+)/$', views.edit_game, name='editGame'),
    url(r'^addGame/(?P<pk>\d+)/$', DetailView.as_view(model=Game, template_name='addgame.html')),
]