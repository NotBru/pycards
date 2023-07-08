from abc import ABC, abstractmethod
from datetime import datetime

from pycards.cards.base import Card


class Scheduler(ABC):
    @abstractmethod
    def deal(self, dt: datetime) -> list[tuple[int, Card]]:
        """Batch-provide indexed cards, according to schedule

        Parameters
        ----------
        dt : datetime
            Current time

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
