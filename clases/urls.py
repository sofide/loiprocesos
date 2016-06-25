from django.conf.urls import include, url
from clases.views import clases_home, clases_add, ver_clase

urlpatterns = [
    url(r'^$', clases_home, name='clases_home'),
    url(r'^cargar$', clases_add, name='clases_add'),
    url(r'^(?P<pk>[0-9]+)/$', ver_clase, name='ver_clase' )

]
