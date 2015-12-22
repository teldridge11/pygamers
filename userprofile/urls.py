from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from models import Game
import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Game.objects.all().order_by('-title'), template_name = 'userprofile.html')),
    url(r'^addGame/$', views.addGame, name='addGame'),
    url(r'^addGame/(?P<pk>\d+)/$', DetailView.as_view(model=Game, template_name='addGame.html')),
]
