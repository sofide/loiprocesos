from django.conf.urls import url
from clases.views import clases_home,  ver_clase, ver_exposicion, preguntas

urlpatterns = [
    url(r'^$', clases_home, name='clases_home'),
    url(r'^(?P<pk>[0-9]+)/$', ver_clase, name='ver_clase'),
    url(r'^exposicion/(?P<expo_pk>[0-9]+)/$', ver_exposicion, name='ver_exposicion'),
    url(r'^preguntas/$', preguntas, name='preguntas'),

]
