from django.conf.urls import url, include
from django.contrib import admin
from base.views import home, pruebas, home_original

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$', home, name='home'),
    url(r'^pruebas/$', pruebas, name='pruebas'),
    url(r'^clases/', include('clases.urls')),
    url(r'^grupos/', include('grupos.urls')),
    url(r'^teoria/', include('teoria.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^1/', home_original, name='home_original'),
    url(r'^2/', home, name='home2'),
]
