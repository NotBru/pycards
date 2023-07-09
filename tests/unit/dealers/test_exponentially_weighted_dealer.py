import pytest
import random
import string

from pycards.dealers.basic import ExponentiallyWeightedDealer
from pycards.cards.static import StaticCard


@pytest.fixture
def deck():
    words = [
        f"{first}{second}{third}"
        for first in string.ascii_uppercase[0:6]
        for second in string.ascii_lowercase[6:12]
        for third in string.digits[0:6]
    ]
    return [StaticCard(w, w) for w in words]


def test_it_deals(deck):
    random.seed(42)

    dealer = ExponentiallyWeightedDealer(deck)
    assert len(dealer.deal(10)) == 10


@pytest.mark.parametrize("lw", [1, 2, 5])
def test_learning_window(deck, lw):
    random.seed(42)

    dealer = ExponentiallyWeightedDealer(deck, learning_window=lw)
    assert all((c in deck[:lw] for _, c in dealer.deal(100)))


def test_learning_reduces_frequency(deck):
    random.seed(42)

    dealer = ExponentiallyWeightedDealer(deck, learning_window=2)
    dealer.update([(0, 0.0)] * 5 + [(1, 1.0)] * 5)
    num_zeroth = sum((c == deck[0] for _, c in dealer.deal(100)))

    assert num_zeroth > 75 and num_zeroth < 100


def test_alpha(deck):
    random.seed(42)

    dealers = [
        ExponentiallyWeightedDealer(deck, alpha=alpha, learning_window=2)
        for alpha in reversed([2 ** (2**i) for i in range(-5, 2)])
    ]
    for dealer in dealers:
        dealer.update([(0, 0.0)] * 3 + [(1, 1.0)] * 3)
    counts = [sum((c == deck[0] for _, c in dealer.deal(10000))) for dealer in dealers]
    for more, less in zip(counts[:-1], counts[1:]):
        assert more > less


@pytest.mark.parametrize("bottom", [-1, -2, -5, -10, -15])
def test_bottom(deck, bottom):
    random.seed(42)

    dealer = ExponentiallyWeightedDealer(deck, learning_window=1, bottom=bottom)
    for i in range(1 - bottom):
        assert dealer.deal(1)[0][1] == deck[0]
        dealer.update([(0, 1.0)])
    assert dealer.deal(1)[0][1] == deck[1]
