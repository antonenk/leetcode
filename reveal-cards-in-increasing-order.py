#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 49% runtime / 97% mem


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()
        result = [deck.pop()]
        while len(deck) > 0:
            lastCard = result.pop()
            result.insert(0, lastCard)
            result.insert(0, deck.pop())

        return result


def test_1():
    assert Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]) == [2, 13, 3, 11, 5, 17, 7]


def test_2():
    assert Solution().deckRevealedIncreasing([1, 1000]) == [1,1000]


if __name__ == '__main__':
    test_1()
    test_2()
