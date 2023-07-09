import random

from pycards.dealers.base import Dealer
from pycards.cards.base import Card


class ExponentiallyWeightedDealer(Dealer):
    def __init__(
        self,
        deck: list[Card],
        learning_window: int = 50,
        alpha: float = 1.3,
        bottom: float = -15.0,
    ):
        self._learning_window = learning_window
        self._deck = {i: card for (i, card) in enumerate(deck)}
        self._weights = {i: 0.0 for i in range(learning_window)}
        self._alpha = alpha
        self._bottom = bottom

    def deal(self, num_cards: int) -> list[tuple[int, Card]]:
        alpha = self._alpha
        indexes = list(self._weights.keys())
        weights = [alpha**exp for exp in self._weights.values()]
        batch = random.choices(
            indexes,
            weights=weights,
            k=num_cards,
        )
        return [(i, self._deck[i]) for i in batch]

    def update(self, performance: list[tuple[int, float]]):
        for i, p in performance:
            self._weights[i] -= (p - 0.5) * 2
        next_ = max(self._weights.keys()) + 1
        self._weights = {i: w for (i, w) in self._weights.items() if w >= self._bottom}
        missing = self._learning_window - len(self._weights)
        top = min(next_ + missing, len(self._deck))
        self._weights.update({i: 0.0 for i in range(next_, top)})
