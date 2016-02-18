from django.conf.urls import include, url
from django.contrib import admin
import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^userprofile/', include('userprofile.urls', namespace='userprofile')),
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)