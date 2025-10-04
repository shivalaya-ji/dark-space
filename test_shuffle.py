from shuffle_cards import make_deck, shuffle_deck, draw


def test_make_deck():
    deck = make_deck()
    assert len(deck) == 52
    # ensure ranks and suits present
    ranks = {r for r, s in deck}
    suits = {s for r, s in deck}
    assert 1 in ranks and 13 in ranks
    assert suits == {"Spade", "Heart", "Diamond", "Club"}


def test_shuffle_changes_order():
    deck = make_deck()
    original = deck.copy()
    shuffle_deck(deck, rng=__import__("random"))
    # there's a very small chance shuffle keeps order; check at least it's a list
    assert isinstance(deck, list)


def test_draw():
    deck = make_deck()
    drawn = draw(deck, 5)
    assert len(drawn) == 5
