from typing import Any, Callable

from pycards.cards.base import Card
from pycards.engines.base import Engine


def _float_eq(left: Any, right: Any) -> float:
    return float(left == right)


class StaticCard(Card):
    def __init__(
        self,
        key: Any,
        value: Any,
        metric: Callable[[Any, Any], float] = _float_eq,
    ):
        self._key = key
        self._value = value
        self._metric = metric

    def prompt(self, engine: Engine) -> float:
        engine.show(self._key)
        value = self._value
        response = engine.fetch(type(value))
        return self._metric(response, value)


def construct_deck(
    samples: list[tuple[Any, Any]],
    symmetric: bool = False,
    metric: Callable[[str, str], float] = _float_eq,
):
    return [StaticCard(k, v, metric) for (k, v) in samples] + (
        [StaticCard(v, k, metric) for (k, v) in samples] if symmetric else []
    )
