from typing import Any

from pycards.engines.base import Engine


class BasicTerminal(Engine):
    def __init__(self):
        self._id = -1

    @property
    def supported_output(self) -> tuple[type]:
        return (str,)

    @property
    def supported_input(self) -> tuple[type]:
        return (str,)

    def _show(self, element: Any) -> int:
        print(element, end="")
        self._id += 1
        return self._id

    def remove(self, element_id: int):
        pass

    def _fetch(self, kind: type, msg: str = "") -> Any:
        msg = msg if not msg else f"{msg}: "
        return input(f"{msg}: " if msg else "")
