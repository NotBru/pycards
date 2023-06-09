import io

import pytest

from pycards.cards.static import StaticCard
from pycards.backends.terminal import BasicTerminal
from pycards.utils.testing import replace_stdin
from pycards.utils.metrics.text_only import string_ratio
from pycards.utils.metrics.generic import float_eq


@pytest.fixture
def backend():
    return BasicTerminal()


def test_text_key_show(backend, capsys):
    expected = "Sarasa: "

    card = StaticCard(expected, "")

    with replace_stdin(io.StringIO("Something")):
        card.prompt(backend)

    actual = capsys.readouterr().out

    assert actual == expected


def test_text_value_gradient(backend):
    real = "the true value"
    card = StaticCard("Key: ", real, string_ratio)

    answers = [real, "the turue value", "cows"]
    rankings = []
    for ans in answers:
        with replace_stdin(io.StringIO(ans)):
            rankings.append(card.prompt(backend))

    assert rankings[0] == 1.0
    for best, worst in zip(rankings[:-1], rankings[1:]):
        assert best > worst


def test_text_value_binary(backend):
    real = "the true value"
    card = StaticCard("Key: ", real, float_eq)

    answers = [real, "the turue value", "cows"]
    rankings = []
    for ans in answers:
        with replace_stdin(io.StringIO(ans)):
            rankings.append(card.prompt(backend))

    assert rankings[0] == 1.0
    assert all([rk == 0.0 for rk in rankings[1:]])
