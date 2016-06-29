from django.conf.urls import url, include
from django.contrib import admin
from base.views import home, pruebas

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$', home, name='home'),
    url(r'^pruebas/$', pruebas, name='pruebas'),
    url(r'^clases/', include('clases.urls')),
    url(r'^grupos/', include('grupos.urls')),
]
