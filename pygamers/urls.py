from django.conf.urls import include, url, patterns
from django.contrib import admin
import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^userprofile/', include('userprofile.urls', namespace="userprofile")),
    url(r'^games/', include('games.urls', namespace="games")),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )