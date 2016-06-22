from django.conf.urls import include, url
from clases import views

urlpatterns = [
    url(r'^$', views.clases_principal, name='clases_principal'),

]
