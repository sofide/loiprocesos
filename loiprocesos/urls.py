from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^clases/', include('clases.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]
