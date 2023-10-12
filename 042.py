import os

TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)]


def solution():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    words_file_path = os.path.join(script_dir, "words.txt")

    words = ""
    with open(words_file_path) as f:
        words = f.readline()

    words = [word.strip('"') for word in words.strip("\r\n").split(",")]
    words = [
        word
        for word in [sum(ord(x) - 64 for x in word) for word in words]
        if word in TRIANGULAR_NUMBERS
    ]
    return len(words)

print(solution())
