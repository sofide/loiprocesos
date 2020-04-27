import pytest

from teoria.models import Pregunta, Unidad
from utils.order_logic import get_previous_and_next_ids, switch_order, update_order

PREGUNTA_1 = Pregunta(pk=1)
PREGUNTA_5 = Pregunta(pk=5)
PREGUNTA_43 = Pregunta(pk=43)


PREVIOUS_AND_NEXT_CASES = [
    # empty list should return an empty list
    ([], []),
    # single element should return the same element with None and None
    ([PREGUNTA_1], [(PREGUNTA_1, None, None)]),
    # example with two elements
    ([PREGUNTA_5, PREGUNTA_1], [(PREGUNTA_5, None, 1), (PREGUNTA_1, 5, None)]),
    # example with three elements
    ([PREGUNTA_1, PREGUNTA_5, PREGUNTA_43], [
        (PREGUNTA_1, None, 5), (PREGUNTA_5, 1, 43), (PREGUNTA_43, 5, None)
    ]),
]


@pytest.mark.parametrize("param,expected", PREVIOUS_AND_NEXT_CASES)
def test_get_previous_and_next_ids(param, expected):
    result = get_previous_and_next_ids(param)

    assert result == expected


def test_switch_order(mocker):
    mecanizado = Unidad(titulo="mecanizado")
    pregunta_1 = Pregunta(orden=1, unidad=mecanizado)
    pregunta_2 = Pregunta(orden=2, unidad=mecanizado)

    mocker.patch.object(pregunta_1, "save")
    mocker.patch.object(pregunta_2, "save")

    switch_order(pregunta_1, pregunta_2)

    assert pregunta_1.orden == 2
    assert pregunta_2.orden == 1

    pregunta_1.save.assert_called_once()
    pregunta_2.save.assert_called_once()


def test_update_order(mocker):
    pregunta_1 = Pregunta(orden=1)
    pregunta_2 = Pregunta(orden=2)
    pregunta_3 = Pregunta(orden=3)

    # precondition
    assert pregunta_1.orden == 1
    assert pregunta_2.orden == 2
    assert pregunta_3.orden == 3

    queryset = [pregunta_3, pregunta_1, pregunta_2]

    for pregunta in queryset:
        mocker.patch.object(pregunta, "save")

    mocker.patch.object(Pregunta, "objects")
    Pregunta.objects.filter.return_value = queryset

    update_order(Pregunta, "mecanizado")

    assert pregunta_1.orden == 1
    assert pregunta_2.orden == 2
    assert pregunta_3.orden == 0

    # save method should not be called in the instances that weren't change
    pregunta_1.save.assert_not_called()
    pregunta_2.save.assert_not_called()

    # the 'orden' attr of pregunta_3 did change, so 'save' method should be called
    pregunta_3.save.assert_called_once()

    Pregunta.objects.filter.assert_called_once_with(unidad="mecanizado")
