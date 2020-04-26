import pytest

from teoria.models import Pregunta
from utils.order_logic import get_previous_and_next_ids

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

