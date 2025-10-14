#!/usr/bin/python3

# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
# beats 82% runtime / 11% mem


class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        playersNum = len(players)
        trainersNum = len(trainers)
        playerId = 0
        trainerId = 0
        matchesNum = 0
        while playerId < playersNum and trainerId < trainersNum:
            if players[playerId] <= trainers[trainerId]:
                playerId += 1
                trainerId += 1
                matchesNum += 1
            else:
                while trainerId < trainersNum and players[playerId] > trainers[trainerId]:
                    trainerId += 1

        return matchesNum


def test_1():
    assert Solution().matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]) == 2


def test_2():
    assert Solution().matchPlayersAndTrainers([1, 1, 1], [10]) == 1


if __name__ == '__main__':
    test_1()
    test_2()
