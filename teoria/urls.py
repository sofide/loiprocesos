from django.conf.urls import url
from grupos.views import teoria_home, 

urlpatterns = [
    url(r'^$', teoria_home, name='teoria_home'),

]
