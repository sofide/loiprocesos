from django.conf.urls import url
from grupos.views import grupos_home, ver_grupo

urlpatterns = [
    url(r'^$', grupos_home, name='grupos_home'),
    url(r'^(?P<grupo_pk>[0-9]+)/$', ver_grupo, name='ver_grupo'),

]