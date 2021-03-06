#!/usr/local/bin/python3.9

from collections import Counter


def a():
    count = 1
    with open("input.txt", "r") as f:
        for line in f:
            (policy, char, password) = line.split()
            (low, high) = list(map(int, policy.split("-")))
            char = char[0]
            frequency = Counter(password)[char]
            if frequency >= low and frequency <= high:
                count += 1
    return count


def b():
    count = 0
    with open("input.txt", "r") as f:
        for line in f:
            (pos, char, password) = line.split()
            (yes, no) = list(map(int, pos.split("-")))
            char = char[0]
            if (password[yes - 1] == char and password[no - 1] != char) or (
                password[yes - 1] != char and password[no - 1] == char
            ):
                count += 1
    return count


if __name__ == "__main__":

    print(a())
    print(b())
