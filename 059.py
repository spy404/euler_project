from __future__ import annotations

import string
from itertools import cycle, product
from pathlib import Path

VALID_CHARS: str = (
    string.ascii_letters + string.digits + string.punctuation + string.whitespace
)
LOWERCASE_INTS: list[int] = [ord(letter) for letter in string.ascii_lowercase]
VALID_INTS: set[int] = {ord(char) for char in VALID_CHARS}

COMMON_WORDS: list[str] = ["the", "be", "to", "of", "and", "in", "that", "have"]


def try_key(ciphertext: list[int], key: tuple[int, ...]) -> str | None:
    decoded: str = ""
    keychar: int
    cipherchar: int
    decodedchar: int

    for keychar, cipherchar in zip(cycle(key), ciphertext):
        decodedchar = cipherchar ^ keychar
        if decodedchar not in VALID_INTS:
            return None
        decoded += chr(decodedchar)

    return decoded


def filter_valid_chars(ciphertext: list[int]) -> list[str]:
    possibles: list[str] = []
    for key in product(LOWERCASE_INTS, repeat=3):
        encoded = try_key(ciphertext, key)
        if encoded is not None:
            possibles.append(encoded)
    return possibles


def filter_common_word(possibles: list[str], common_word: str) -> list[str]:
    return [possible for possible in possibles if common_word in possible.lower()]


def solution(filename: str = "p059_cipher.txt") -> int:
    ciphertext: list[int]
    possibles: list[str]
    common_word: str
    decoded_text: str
    data: str = Path(__file__).parent.joinpath(filename).read_text(encoding="utf-8")

    ciphertext = [int(number) for number in data.strip().split(",")]

    possibles = filter_valid_chars(ciphertext)
    for common_word in COMMON_WORDS:
        possibles = filter_common_word(possibles, common_word)
        if len(possibles) == 1:
            break

    decoded_text = possibles[0]
    return sum(ord(char) for char in decoded_text)

print(f"{solution() = }")
