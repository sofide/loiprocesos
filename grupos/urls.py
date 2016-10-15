from django.conf.urls import url
from grupos.views import grupos_home, ver_grupo, edit_grupo, dashboard,\
     dashboard_grupo, autoevaluacion, ver_autoevaluacion


urlpatterns = [
    url(r'^$', grupos_home, name='grupos_home'),
    url(r'^(?P<grupo_pk>[0-9]+)/$', ver_grupo, name='ver_grupo'),
    url(r'^(?P<grupo_pk>[0-9]+)/edit$', edit_grupo, name='edit_grupo'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^dashboard/(?P<grupo_pk>[0-9]+)/$', dashboard_grupo, name='dashboard_grupo'),
    url(r'^autoevaluacion/$', autoevaluacion, name='autoevaluacion'),
    url(r'^autoevaluacion/(?P<autoevaluacion_pk>[0-9]+)/$', ver_autoevaluacion, name='ver_autoevaluacion'),


]
