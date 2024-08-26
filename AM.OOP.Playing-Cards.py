# AM OOP Design
# Playing Card
# https://algo.monster/problems/oop_playing_cards
from typing import Dict, List

CARD_VALUES: Dict[str, int] = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
}


class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit: str = suit
        self.value: str = value

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"

    def __hash__(self) -> str:
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.suit, self.value))

    def __eq__(self, other: "Card") -> bool:
        return self.suit == other.suit and self.value == other.value

    def __lt__(self, other: "Card") -> bool:
        return CARD_VALUES[self.value] < CARD_VALUES[other.value]


class Game:
    def __init__(self) -> None:
        self.card_deck: List[Card] = []

    def add_card(self, suit: str, value: str) -> None:
        """Create a new card object and add it to the Game card deck"""
        self.card_deck.append(Card(suit=suit, value=value))

    def card_string(self, card: int) -> str:
        """Returns the string representation of the card represented by card

        Args
            card: the index of a card in card_deck
        """
        return str(self.card_deck[card])

    def card_beats(self, card_a: int, card_b: int) -> bool:
        """Check if the card represented by card_a beats the one represented by card_b.

        Args
            card_a: the index of a card in card_deck
            card_b: the index of a card in card_deck

        Returns
            True if card_a beats card_b, False otherwise
        """
        return self.card_deck[card_a] > self.card_deck[card_b]
