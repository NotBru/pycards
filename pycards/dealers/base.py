from abc import ABC, abstractmethod

from pycards.cards.base import Card


class Dealer(ABC):
    @abstractmethod
    def deal(self, num_cards: int) -> list[tuple[int, Card]]:
        """Batch-provide indexed cards

        Parameters
        ----------
        num_cards : int
            Number of cards to deal

        Returns
        -------
        [(idx, card)]
            card : Card
            idx : Card index, for later feedback
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, performance: list[tuple[int, float]]):
        """Update knowledge of user performance

        Parameters
        ----------
        performance : list[tuple[int, float]]
            [(idx, perf)] where perf is the performance during card prompt
        """
        raise NotImplementedError
