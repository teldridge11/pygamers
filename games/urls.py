from django.conf.urls import url, patterns
import views
from django.views.generic import ListView, DetailView
from userprofile.models import Game

urlpatterns = [
    url(r'^$', views.games_view, name='games_view'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Game, template_name='gameprofile.html')),
]