# AM OOP Design
# Playing Card
# https://algo.monster/problems/oop_playing_cards
from abc import ABC, abstractmethod
from typing import Dict, List


class Card(ABC):
    @property
    @abstractmethod
    def value(self) -> int:
        """An abstract property representing the card value"""
        raise NotImplementedError

    def __lt__(self, other: "Card") -> bool:
        return self.value < other.value


class PlayingCard(Card):
    """A sub class of Card representing a playing card with its suit and value"""

    PLAYING_CARD_VALUES: Dict[str, int] = {
        "A": 1,
        **{str(i): i for i in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
    }

    def __init__(self, suit: str, value: str) -> None:
        self.__suit: str = suit
        self.__value: str = value

    @property
    def value(self) -> int:
        """A property representing the card value"""
        return self.PLAYING_CARD_VALUES[self.__value]

    @property
    def suit(self) -> str:
        """A property representing the card suit"""
        return self.__suit

    def __str__(self) -> str:
        return f"{self.__value} of {self.__suit}"

    def __hash__(self) -> str:
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.__suit, self.__value))

    def __eq__(self, other: "PlayingCard") -> bool:
        return self.suit == other.suit and self.value == other.value


class Game:
    def __init__(self) -> None:
        self.card_deck: List[PlayingCard] = []

    def add_card(self, suit: str, value: str) -> None:
        """Create a new card object and add it to the Game card deck

        Args:
            suit: the card suit
            value: the card value
        """
        self.card_deck.append(PlayingCard(suit=suit, value=value))

    def add_joker(self, color: str) -> None:
        """Create a new joker card object and add it to the Game card deck

        Args:
            color: the joker card color
        """
        pass

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


if __name__ == "__main__":
    game = Game()
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(0))
    suit, value = input().split()
    game.add_card(suit, value)
    print(game.card_string(1))
    print("true" if game.card_beats(0, 1) else "false")
