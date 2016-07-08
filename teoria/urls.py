from django.conf.urls import url
from teoria.views import teoria_home, ver_unidad, add_unidad

urlpatterns = [
    url(r'^$', teoria_home, name='teoria_home'),
    url(r'^$', add_unidad, name='add_unidad'),
    url(r'^(?P<unidad_pk>[0-9]+)/$', ver_unidad, name='ver_unidad'),

]
