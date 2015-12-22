from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^userprofile/', include('userprofile.urls', namespace="userprofile")),
    url(r'^admin/', admin.site.urls),
]
