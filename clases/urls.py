from django.conf.urls import url
from clases.views import (clases_home,  ver_clase, ver_exposicion, preguntas,
                          trabajos_practicos, edit_tp, edit_text, ver_tp,
                          votar_preg, virtual_expo)

urlpatterns = [
    url(r'^$', clases_home, name='clases_home'),
    url(r'^(?P<pk>[0-9]+)/$', ver_clase, name='ver_clase'),
    url(r'^exposicion/(?P<expo_pk>[0-9]+)/$', ver_exposicion, name='ver_exposicion'),
    url(r'^preguntas/$', preguntas, name='preguntas'),
    url(r'^tp/$', trabajos_practicos, name='trabajos_practicos'),
    url(r'^tp/edit/(?P<tp_pk>[0-9]+)?/?$', edit_tp, name='edit_tp'),
    url(r'^text/edit/(?P<text_pk>[0-9]+)?/?$', edit_text, name='edit_text'),
    url(r'^tp/(?P<tp_pk>[0-9]+)/$', ver_tp, name='ver_tp'),
    url(r'^votar/(?P<preg_pk>[0-9]+)/(?P<voto>[+-])/$', votar_preg, name='votar_preg'),
    url(r'^vexpo/$', virtual_expo, name='virtual_expo'),

]
