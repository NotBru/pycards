from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Weekpoint:
    day_of_week: int
    hour: int
    minute: int
    second: int


class Scheduler(ABC):
    @abstractmethod
    def load(self, dt: datetime) -> int:
        """Provide number of extra cards to deal, according to some schedule

        Parameters
        ----------
        dt : datetime
            Current time

        Returns
        -------
        int
            Number of cards to deal
        """
        raise NotImplementedError
