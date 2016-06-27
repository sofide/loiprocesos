from django.conf.urls import url, include
from django.contrib import admin
from base.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^$', home, name='home'),
    url(r'^clases/', include('clases.urls')),
    url(r'^grupos/', include('grupos.urls')),
]
