from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^auth/$', views.login_auth, name='login_auth'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^logout/$', views.logout_user, name='logout'),
]