from django.conf.urls import url
from teoria.views import (teoria_home, ver_unidad, edit_ud, add_recurso, edit_recurso,
                          del_recurso, edit_text, voto_recurso, switch_pregunta)

urlpatterns = [
    url(r'^$', teoria_home, name='teoria_home'),
    url(r'^(?P<unidad_pk>[0-9]+)/$', ver_unidad, name='ver_unidad'),
    url(r'^ud/edit/(?P<ud_pk>[0-9]+)?/?$', edit_ud, name='edit_ud'),
    url(r'^recurso/(?P<recurso>[mp])/$', add_recurso, name='add_recurso'),
    url(r'^recurso/(?P<recurso>[mp])/(?P<ud_pk>[0-9]+)?/$', add_recurso, name='add_recurso_in_ud'),
    url(r'^recurso/editar/(?P<recurso>[mp])/(?P<pk>[0-9]+)?/$', edit_recurso, name='edit_recurso'),
    url(r'^quitar/(?P<recurso>[mp])/(?P<pk>[0-9]+)/$', del_recurso, name='del_recurso'),
    url(r'^text/edit/(?P<text_pk>[0-9]+)?/?$', edit_text, name='edit_text'),
    url(r'^(?P<voto>[+-])/(?P<recurso>[mp])/(?P<rec_pk>[0-9]+)/$', voto_recurso, name='voto_recurso'),
    url(r'^switch/preguntas/(?P<pk_1>[0-9]+)/(?P<pk_2>[0-9]+)/?$', switch_pregunta, name='switch_pregunta'),



]
