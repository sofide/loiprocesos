from django.conf.urls import url
from gallery.views import gallery_home

urlpatterns = [
    url(r'^$', gallery_home, name='gallery_home'),
]
