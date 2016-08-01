from django.conf.urls import url
from teoria.views import (teoria_home, ver_unidad, edit_ud, add_recurso, del_recurso)

urlpatterns = [
    url(r'^$', teoria_home, name='teoria_home'),
    url(r'^(?P<unidad_pk>[0-9]+)/$', ver_unidad, name='ver_unidad'),
    url(r'^ud/edit/(?P<ud_pk>[0-9]+)?/?$', edit_ud, name='edit_ud'),
    url(r'^recurso/(?P<recurso>[mp])/$', add_recurso, name='add_recurso'),
    url(r'^quitar/(?P<recurso>[mp])/(?P<pk>[0-9]+)/$', del_recurso, name='del_recurso'),



]
