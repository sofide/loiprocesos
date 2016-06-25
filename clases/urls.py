from django.conf.urls import include, url
from clases.views import clases_home

urlpatterns = [
    url(r'^$', clases_home, name='clases_home'),
    url(r'^/cargar$', clases_add, name='clases_add'),

]
