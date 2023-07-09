from abc import ABC, abstractmethod
from typing import Any


class Engine(ABC):
    @property
    @abstractmethod
    def supported_output(self) -> tuple[type]:
        raise NotImplementedError

    @property
    @abstractmethod
    def supported_input(self) -> tuple[type]:
        raise NotImplementedError

    @staticmethod
    def _supported_string(types: tuple[type]) -> str:
        comma_separated = ", ".join(
            (f"{class_.__module__}.{class_.__qualname__}" for class_ in types)
        )
        return f"({comma_separated})"

    @abstractmethod
    def _show(self, element: Any) -> int:
        raise NotImplementedError

    def show(self, element: Any, **kwargs) -> int:
        if not isinstance(element, self.supported_output):
            err = (
                "Current engine only supports types in "
                + self._supported_string(self.supported_output)
                + "for output"
            )
            raise TypeError(err)
        return self._show(element, **kwargs)

    @abstractmethod
    def remove(self, element_id: int):
        raise NotImplementedError

    @abstractmethod
    def _fetch(self, kind: type) -> Any:
        raise NotImplementedError

    def fetch(self, kind: type, **kwargs) -> Any:
        if not issubclass(kind, self.supported_input):
            err = (
                "Current engine only supports types in "
                + self._supported_string(self.supported_output)
                + "for input"
            )
            raise TypeError(err)
        fetched = self._fetch(kind, **kwargs)
        assert isinstance(fetched, kind)
        return fetched
