import factory
from factory.django import DjangoModelFactory

from clases import models as class_models
from grupos import models as groups_models
from teoria import models as teoria_models


class ClaseFactory(DjangoModelFactory):
    class Meta:
        model = class_models.Clase


class TPFactory(DjangoModelFactory):
    class Meta:
        model = class_models.TP


class GrupoFactory(DjangoModelFactory):
    class Meta:
        model = groups_models.Grupo

    año = factory.Faker('year')
    numero = factory.Faker('pyint')

class ExposicionFactory(DjangoModelFactory):
    class Meta:
        model = class_models.Exposicion

    grupo = factory.SubFactory(GrupoFactory)
    clase = factory.SubFactory(ClaseFactory)
    tp = factory.SubFactory(TPFactory)


class AutoevaluacionFactory(DjangoModelFactory):
    class Meta:
        model = groups_models.Autoevaluacion_grupal

    año = factory.Faker('year')


class UnidadFactory(DjangoModelFactory):
    class Meta:
        model = teoria_models.Unidad
    numero = factory.Faker('pyint')


class MaterialFactory(DjangoModelFactory):
    class Meta:
        model = teoria_models.Material

    unidad = factory.SubFactory(UnidadFactory)
    fecha = factory.Faker('date')


class PreguntaFactory(DjangoModelFactory):
    class Meta:
        model = teoria_models.Pregunta

    unidad = factory.SubFactory(UnidadFactory)
    fecha = factory.Faker('date')
