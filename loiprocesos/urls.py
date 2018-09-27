from django.conf.urls import url, include
from django.contrib import admin
from base.views import home_dos, pruebas, home_original, home_tres

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$', home_tres, name='home'),
    url(r'^pruebas/$', pruebas, name='pruebas'),
    url(r'^clases/', include('clases.urls')),
    url(r'^grupos/', include('grupos.urls')),
    url(r'^teoria/', include('teoria.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^1/', home_original, name='home_original'),
    url(r'^2/', home_dos, name='home2'),
    url(r'^3/', home_tres, name='home3'),
]
