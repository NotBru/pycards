from typing import Any, Callable

from pycards.cards.base import Card
from pycards.backends.base import Backend
from pycards.utils.metrics.generic import float_eq


class StaticCard(Card):
    def __init__(
        self,
        key: Any,
        value: Any,
        metric: Callable[[Any, Any], float] = float_eq,
    ):
        self._key = key
        self._value = value
        self._metric = metric

    def prompt(self, backend: Backend) -> float:
        backend.show(self._key)
        value = self._value
        response = backend.fetch(type(value))
        return self._metric(response, value)


def construct_deck(
    samples: list[tuple[Any, Any]],
    symmetric: bool = False,
    metric: Callable[[str, str], float] = float_eq,
):
    return [StaticCard(k, v, metric) for (k, v) in samples] + (
        [StaticCard(v, k, metric) for (k, v) in samples] if symmetric else []
    )
