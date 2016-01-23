from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, {'post_reset_redirect' : '/accounts/password_reset_done/'}, name='password_reset'),
    url(r'^password_reset_done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'post_reset_redirect' : '/accounts/password_done/'}, name='password_reset_confirm'),
    url(r'^password_done/$', auth_views.password_reset_complete, name='password_done'),
    url(r'^auth/$', views.login_auth, name='login_auth'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^logout/$', views.logout_user, name='logout'),
]