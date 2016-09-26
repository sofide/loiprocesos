from django.conf.urls import url
from grupos.views import grupos_home, ver_grupo, edit_grupo, dashboard

urlpatterns = [
    url(r'^$', grupos_home, name='grupos_home'),
    url(r'^(?P<grupo_pk>[0-9]+)/$', ver_grupo, name='ver_grupo'),
    url(r'^(?P<grupo_pk>[0-9]+)/edit$', edit_grupo, name='edit_grupo'),
    url(r'^dashboard/$', dashboard, name='dashboard'),

]
