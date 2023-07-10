import io
import pytest

from pycards.backends.terminal import BasicTerminal
from pycards.utils.testing import replace_stdin


@pytest.fixture
def terminal_backend():
    return BasicTerminal()


def test_show_string(terminal_backend, capsys):
    expected = "Some string"

    terminal_backend.show(expected)
    actual = capsys.readouterr().out

    assert actual == expected


def test_show_invalid(terminal_backend):
    with pytest.raises(TypeError):
        terminal_backend.show(1)


def test_remove(terminal_backend):
    terminal_backend.remove(terminal_backend.show("String"))


def test_fetch(terminal_backend):
    expected = "Hai\n"
    with replace_stdin(io.StringIO(expected)):
        actual = terminal_backend.fetch(str)

    assert actual == expected[:-1]
