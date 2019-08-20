import pytest
import datetime as dt

from base.tests import factories
from grupos.models import Pertenencia

MEMBER_USERNAME = 'member name'
MEMBER_PASSWORD = 'member_password'

@pytest.fixture
def member(django_user_model):
    group = factories.GrupoFactory()
    user = django_user_model.objects.create_user(
        username=MEMBER_USERNAME,
        password=MEMBER_PASSWORD
    )
    pertenencia = Pertenencia.objects.create(grupo=group, usuario=user)

    return user


from django.core.urlresolvers import reverse
@pytest.fixture
def member_client(member, client):
    client.login(username=member.username, password=MEMBER_PASSWORD)
    return client
