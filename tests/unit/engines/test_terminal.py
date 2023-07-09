import io
import pytest

from pycards.engines.terminal import BasicTerminal
from pycards.utils.testing import replace_stdin


@pytest.fixture
def terminal_engine():
    return BasicTerminal()


def test_show_string(terminal_engine, capsys):
    expected = "Some string"

    terminal_engine.show(expected)
    actual = capsys.readouterr().out

    assert actual == expected


def test_show_invalid(terminal_engine):
    with pytest.raises(TypeError):
        terminal_engine.show(1)


def test_remove(terminal_engine):
    terminal_engine.remove(terminal_engine.show("String"))


def test_fetch(terminal_engine):
    expected = "Hai\n"
    with replace_stdin(io.StringIO(expected)):
        actual = terminal_engine.fetch(str)

    assert actual == expected[:-1]
