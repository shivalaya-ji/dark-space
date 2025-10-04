"""Shuffle a deck of cards and draw cards.

Provides functions for testing:
- make_deck() -> list of (rank, suit)
- shuffle_deck(deck, *, rng=random) -> None (in-place)
- draw(deck, n=5) -> list of cards

Running the file prints five drawn cards.
"""

import itertools
import random
from typing import List, Tuple


Card = Tuple[int, str]


def make_deck() -> List[Card]:
    """Create a standard 52-card deck as (rank, suit) tuples."""
    return list(
        itertools.product(range(1, 14), ("Spade", "Heart", "Diamond", "Club"))
    )


def shuffle_deck(deck: List[Card], rng=random) -> None:
    """Shuffle the deck in-place. `rng` is the random module or a Random instance."""
    rng.shuffle(deck)


def draw(deck: List[Card], n: int = 5) -> List[Card]:
    """Draw the top n cards from the deck (does not modify deck)."""
    return deck[:n]


if __name__ == "__main__":
    deck = make_deck()
    shuffle_deck(deck)
    print("You got:")
    for rank, suit in draw(deck, 5):
        print(rank, "of", suit)
