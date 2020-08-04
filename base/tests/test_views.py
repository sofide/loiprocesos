import pytest
from django.core.urlresolvers import reverse

from base.tests import factories


RESPONSE_STATUS_CODE_OK = 200


def get_kwargs(kwargs_list, group_member=None):
    kwargs = {}
    if group_member:
        group = group_member.grupos.first()
    for key, value in kwargs_list:
        if group_member and value == factories.GrupoFactory:
            value = group.pk
        elif hasattr(value, '__call__'):
            value = value().pk
        kwargs[key] = value

    return kwargs


PUBLIC_ACCESS_VIEW = [
    # defined in loiprocesos.urls
    ('home', []),
    ('feedback', []),
    # defined in clases.urls
    ('clases_home', []),
    ('ver_clase', [('pk', factories.ClaseFactory)]),
    ('ver_exposicion', [('expo_pk', factories.ExposicionFactory)]),
    ('preguntas', [('expo_pk', factories.ExposicionFactory)]),
    ('trabajos_practicos', []),
    ('ver_tp', [('tp_pk', factories.TPFactory)]),
    # defined in grupos.urls
    ('grupos_home', []),
    ('ver_grupo', [('grupo_pk', factories.GrupoFactory)]),
    ('ver_autoevaluacion', [('autoevaluacion_pk', factories.AutoevaluacionFactory)]),
    ('cargar_autoevaluacion', [('autoevaluacion_pk', factories.AutoevaluacionFactory)]),
    ('dashboard', []),
    ('dashboard_grupo', [('grupo_pk', factories.GrupoFactory)]),
    # defined in teoria.urls
    ('teoria_home', []),
    ('ver_unidad', [('unidad_pk', factories.UnidadFactory)]),
    ('add_recurso_in_ud', [('recurso', 'm'), ('ud_pk', factories.UnidadFactory)]), # add new material
    ('add_recurso_in_ud', [('recurso', 'p'), ('ud_pk', factories.UnidadFactory)]), # add new question
]


@pytest.mark.slow
@pytest.mark.django_db
@pytest.mark.parametrize('url_name,kwargs', PUBLIC_ACCESS_VIEW)
def test_public_views_are_working(url_name, kwargs, client):
    kwargs = get_kwargs(kwargs)
    response = client.get(reverse(url_name, kwargs=kwargs))

    assert response.status_code == RESPONSE_STATUS_CODE_OK


STAFF_ACCESS_VIEWS = [
    # defined in  clases.url
    ('edit_tp', []),
    ('edit_text', []),
    # defined in teoria.urls
    ('edit_ud', [('ud_pk', factories.UnidadFactory)]),
]


@pytest.mark.slow
@pytest.mark.parametrize('url_name,kwargs', STAFF_ACCESS_VIEWS)
def test_staff_views_are_working(url_name, kwargs, admin_client):
    kwargs = get_kwargs(kwargs)
    response = admin_client.get(reverse(url_name, kwargs=kwargs))

    assert response.status_code == RESPONSE_STATUS_CODE_OK


@pytest.mark.slow
@pytest.mark.django_db
@pytest.mark.parametrize('url_name,kwargs', STAFF_ACCESS_VIEWS)
def test_staff_views_prohibit_for_non_staff_users(url_name, kwargs, client):
    kwargs = get_kwargs(kwargs)
    response = client.get(reverse(url_name, kwargs=kwargs))

    assert response.status_code != RESPONSE_STATUS_CODE_OK


MEMBER_ACCESS_VIEWS = [
    # defined in  clases.url
    ('virtual_expo', []),
    # defined in  grupos.url
    ('edit_grupo', [('grupo_pk', factories.GrupoFactory)]),
    ('carga_autoevaluacion', [
        ('autoevaluacion_pk', factories.AutoevaluacionFactory),
        ('grupo_evaluador_pk', factories.GrupoFactory)
    ]),
]


@pytest.mark.slow
@pytest.mark.parametrize('url_name,kwargs', MEMBER_ACCESS_VIEWS)
def test_member_views_are_working(url_name, kwargs, member, member_client):
    kwargs = get_kwargs(kwargs, group_member=member)
    response = member_client.get(reverse(url_name, kwargs=kwargs))

    assert response.status_code == RESPONSE_STATUS_CODE_OK


@pytest.mark.slow
@pytest.mark.django_db
@pytest.mark.parametrize('url_name,kwargs', STAFF_ACCESS_VIEWS)
def test_member_views_prohibit_for_non_group_member_users(url_name, kwargs, client):
    kwargs = get_kwargs(kwargs)
    response = client.get(reverse(url_name, kwargs=kwargs))

    assert response.status_code != RESPONSE_STATUS_CODE_OK
