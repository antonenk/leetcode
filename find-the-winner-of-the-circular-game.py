#!/usr/bin/python3

# https://leetcode.com/problems//description/
# beats 32% runtime / 21% mem


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i + 1 for i in range(n)]
        currentId = 0
        for step in range(n - 1):
            looserId = (currentId + k - 1) % len(players)
            players.remove(players[looserId])
            currentId = looserId
        return players[0]


def test_1():
    assert Solution().findTheWinner(5, 2) == 3


def test_2():
    assert Solution().findTheWinner(6, 5) == 1


if __name__ == '__main__':
    test_1()
    test_2()
