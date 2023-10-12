from __future__ import annotations

import os


class PokerHand:
    _HAND_NAME = (
        "High card",
        "One pair",
        "Two pairs",
        "Three of a kind",
        "Straight",
        "Flush",
        "Full house",
        "Four of a kind",
        "Straight flush",
        "Royal flush",
    )

    _CARD_NAME = (
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )

    def __init__(self, hand: str) -> None:
        if not isinstance(hand, str):
            msg = f"Hand should be of type 'str': {hand!r}"
            raise TypeError(msg)
        if len(hand.split(" ")) != 5:
            msg = f"Hand should contain only 5 cards: {hand!r}"
            raise ValueError(msg)
        self._hand = hand
        self._first_pair = 0
        self._second_pair = 0
        self._card_values, self._card_suit = self._internal_state()
        self._hand_type = self._get_hand_type()
        self._high_card = self._card_values[0]

    @property
    def hand(self):
        return self._hand

    def compare_with(self, other: PokerHand) -> str:
        if self._hand_type > other._hand_type:
            return "Win"
        elif self._hand_type < other._hand_type:
            return "Loss"
        elif self._first_pair == other._first_pair:
            if self._second_pair == other._second_pair:
                return self._compare_cards(other)
            else:
                return "Win" if self._second_pair > other._second_pair else "Loss"
        return "Win" if self._first_pair > other._first_pair else "Loss"

    def hand_name(self) -> str:
        name = PokerHand._HAND_NAME[self._hand_type - 14]
        high = PokerHand._CARD_NAME[self._high_card]
        pair1 = PokerHand._CARD_NAME[self._first_pair]
        pair2 = PokerHand._CARD_NAME[self._second_pair]
        if self._hand_type in [22, 19, 18]:
            return name + f", {high}-high"
        elif self._hand_type in [21, 17, 15]:
            return name + f", {pair1}s"
        elif self._hand_type in [20, 16]:
            join = "over" if self._hand_type == 20 else "and"
            return name + f", {pair1}s {join} {pair2}s"
        elif self._hand_type == 23:
            return name
        else:
            return name + f", {high}"

    def _compare_cards(self, other: PokerHand) -> str:
        for index, card_value in enumerate(self._card_values):
            if card_value != other._card_values[index]:
                return "Win" if card_value > other._card_values[index] else "Loss"
        return "Tie"

    def _get_hand_type(self) -> int:
        if self._is_flush():
            if self._is_five_high_straight() or self._is_straight():
                return 23 if sum(self._card_values) == 60 else 22
            return 19
        elif self._is_five_high_straight() or self._is_straight():
            return 18
        return 14 + self._is_same_kind()

    def _is_flush(self) -> bool:
        return len(self._card_suit) == 1

    def _is_five_high_straight(self) -> bool:
        if sorted(self._card_values) == [2, 3, 4, 5, 14]:
            if self._card_values[0] == 14:
                ace_card = self._card_values.pop(0)
                self._card_values.append(ace_card)
            return True
        return False

    def _is_straight(self) -> bool:
        for i in range(4):
            if self._card_values[i] - self._card_values[i + 1] != 1:
                return False
        return True

    def _is_same_kind(self) -> int:
        kind = val1 = val2 = 0
        for i in range(4):
            if self._card_values[i] == self._card_values[i + 1]:
                if not val1:
                    val1 = self._card_values[i]
                    kind += 1
                elif val1 == self._card_values[i]:
                    kind += 2
                elif not val2:
                    val2 = self._card_values[i]
                    kind += 1
                elif val2 == self._card_values[i]:
                    kind += 2
        kind = kind + 2 if kind in [4, 5] else kind
        first = max(val1, val2)
        second = min(val1, val2)
        if kind == 6 and self._card_values.count(first) != 3:
            first, second = second, first
        self._first_pair = first
        self._second_pair = second
        return kind

    def _internal_state(self) -> tuple[list[int], set[str]]:
        trans: dict = {"T": "10", "J": "11", "Q": "12", "K": "13", "A": "14"}
        new_hand = self._hand.translate(str.maketrans(trans)).split()
        card_values = [int(card[:-1]) for card in new_hand]
        card_suit = {card[-1] for card in new_hand}
        return sorted(card_values, reverse=True), card_suit

    def __repr__(self):
        return f'{self.__class__}("{self._hand}")'

    def __str__(self):
        return self._hand

    def __eq__(self, other):
        if isinstance(other, PokerHand):
            return self.compare_with(other) == "Tie"
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, PokerHand):
            return self.compare_with(other) == "Loss"
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, PokerHand):
            return self < other or self == other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, PokerHand):
            return not self < other and self != other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, PokerHand):
            return not self < other
        return NotImplemented

    def __hash__(self):
        return object.__hash__(self)


def solution() -> int:
    answer = 0
    script_dir = os.path.abspath(os.path.dirname(__file__))
    poker_hands = os.path.join(script_dir, "poker_hands.txt")
    with open(poker_hands) as file_hand:
        for line in file_hand:
            player_hand = line[:14].strip()
            opponent_hand = line[15:].strip()
            player, opponent = PokerHand(player_hand), PokerHand(opponent_hand)
            output = player.compare_with(opponent)
            if output == "Win":
                answer += 1
    return answer


solution()
