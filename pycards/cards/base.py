from abc import ABC, abstractmethod

from pycards.backends.base import Backend


class Card(ABC):
    @abstractmethod
    def prompt(self, backend: Backend) -> float:
        """Prompt user for a challenge and evaluate response

        Returns
        -------
        performance : float
            User performance throughout task, on a scale from 0. to 1.
        """
        raise NotImplementedError
